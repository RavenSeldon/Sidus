import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const host = '0.0.0.0';
const port = Number(process.env.PORT || 3000);

if (!Number.isInteger(port) || port < 1 || port > 65535) {
  throw new Error(`Invalid PORT: ${process.env.PORT}`);
}

const types = {
  '.css': 'text/css; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.jpeg': 'image/jpeg',
  '.jpg': 'image/jpeg',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.mp4': 'video/mp4',
  '.pdf': 'application/pdf',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.tsv': 'text/tab-separated-values; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.webmanifest': 'application/manifest+json',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.xml': 'application/xml; charset=utf-8'
};

const securityHeaders = {
  'content-security-policy': "default-src 'self'; img-src 'self' data: https: *; style-src 'self' 'unsafe-inline' https: *; script-src 'self' 'unsafe-inline' https: *; font-src 'self' data: https: *; connect-src 'self' https: *; media-src 'self' https: *; object-src 'none'; frame-src 'self' https: *;",
  'referrer-policy': 'strict-origin-when-cross-origin',
  'x-content-type-options': 'nosniff',
  'x-xss-protection': '1; mode=block'
};

function fail(res, status, message, extra = {}) {
  res.writeHead(status, { ...securityHeaders, ...extra, 'content-type': 'text/plain; charset=utf-8' });
  res.end(message);
}

const server = http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    return fail(res, 405, 'method not allowed', { allow: 'GET, HEAD' });
  }

  let pathname;
  try {
    pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  } catch {
    return fail(res, 400, 'bad request');
  }

  let file = path.resolve(root, `.${pathname}`);
  if (file !== root && !file.startsWith(`${root}${path.sep}`)) return fail(res, 403, 'forbidden');

  try {
    if (fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  } catch {
    return fail(res, 404, 'not found');
  }

  let stat;
  try {
    stat = fs.statSync(file);
  } catch {
    return fail(res, 404, 'not found');
  }
  if (!stat.isFile()) return fail(res, 404, 'not found');

  const headers = {
    ...securityHeaders,
    'accept-ranges': 'bytes',
    'cache-control': 'no-cache',
    'content-type': types[path.extname(file).toLowerCase()] || 'application/octet-stream',
    'last-modified': stat.mtime.toUTCString()
  };

  let start = 0;
  let end = stat.size - 1;
  let status = 200;
  const range = req.headers.range?.match(/^bytes=(\d*)-(\d*)$/);
  if (req.headers.range && !range) {
    return fail(res, 416, 'range not satisfiable', { 'content-range': `bytes */${stat.size}` });
  }
  if (range) {
    if (range[1]) start = Number(range[1]);
    if (range[2]) end = Number(range[2]);
    if (!range[1] && range[2]) start = Math.max(0, stat.size - Number(range[2]));
    if (start > end || start >= stat.size || !Number.isSafeInteger(start) || !Number.isSafeInteger(end)) {
      return fail(res, 416, 'range not satisfiable', { 'content-range': `bytes */${stat.size}` });
    }
    end = Math.min(end, stat.size - 1);
    status = 206;
    headers['content-range'] = `bytes ${start}-${end}/${stat.size}`;
  }
  headers['content-length'] = String(end - start + 1);

  res.writeHead(status, headers);
  if (req.method === 'HEAD') return res.end();
  const stream = fs.createReadStream(file, { start, end });
  stream.on('error', () => res.destroy());
  stream.pipe(res);
});

server.listen(port, host, () => {
  console.log(`Sīdus static server listening on ${host}:${port}`);
});

function shutdown() {
  server.close(() => process.exit(0));
}
process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
