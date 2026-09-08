SĪDUS WEB INTERFACE

Open index.html in any modern browser.
For easiest hosting, upload Sidus_Dossier_Standalone.html together with the source/ directory. The PDF and Markdown reader links use the canonical filenames in source/; keep those filenames unchanged and ensure these are the updated final files you intend to serve.

Opening Sidus_Dossier_Standalone.html by itself will display the dossier, but its PDF and Markdown links require the adjacent source/ directory.

Atlas plates can be expanded by clicking/tapping them or pressing Enter/Space while focused. Close the expanded plate with Escape, the × button, or by clicking/tapping outside the plate.

The source/ directory contains the four canonical Markdown documents and their synchronized PDFs. The September 2026 revision applies the R9-R14 implementation-validity corrections and makes the Tractable Horizon university agnostic. The research scope remains frozen outside those authorized changes.

REBUILDING

Run python scripts/rebuild.py to regenerate the website readers, PDF bodies and SOURCE_SHA256.txt from source/*.md. Requirements: Pandoc 3.x, XeLaTeX with the packages in scripts/pdf-style.tex, DejaVu fonts, Latin Modern Math, and Python packages pymupdf and pypdf. Run python scripts/rebuild.py --web-only when only the web reader needs rebuilding; regenerate PDFs before releasing source-text changes.

The existing cover artwork is retained in scripts/covers/. The plain-language companion remains editorial content inside assets/content.js; update it when a source correction changes its explanation. The rebuild copies the same document/companion data and application scripts into the standalone reader. Refresh the sw.js cache version for each release. Hosting remains a static-file deployment; this change introduces no server or hosting dependency.

E0-A FIELD REPORT (dated companion, 7 September 2026)

Results is available at #/results, with the walkthrough at #/results/e0-a.
The script-free reading edition is e0a.html. See E0A_HANDOVER.md for the
companion-only build/check commands and preserved-source hashes. Do not run
canonical document/PDF regeneration to update the experimental companion.
