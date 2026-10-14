// One command to keep every language in step with the English site:
//   node scripts/i18n/sync.mjs [--backend auto|claude|api|packets] [--render]
// extract (find every English unit) → translate (only what is new or changed) → build → check.
import { spawnSync } from 'node:child_process';
import { rel } from './lib.mjs';
const args = process.argv.slice(2);
const pass = name => { const i = args.indexOf('--' + name); return i < 0 ? [] : ['--' + name, args[i + 1]]; };
const steps = [
  ['extract.mjs'],
  ['translate.mjs', ...pass('backend'), ...pass('wave')],
  ['build.mjs'],
  ['check.mjs', ...(args.includes('--render') ? ['--render'] : [])]
];
for (const [script, ...rest] of steps) {
  console.log(`\n── ${script} ${rest.join(' ')}`);
  const r = spawnSync(process.execPath, [rel('scripts/i18n', script), ...rest], { stdio: 'inherit', cwd: rel() });
  if (r.status !== 0) { console.error(`Stopped: ${script} failed.`); process.exit(r.status || 1); }
}
