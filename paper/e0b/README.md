# E0-B paper source

`Sidus_E0B_Research_Paper.source.md` is the 8 October 2026 paper text plus the release changes listed in the E0-B publication addendum. Those changes are the DOI line on the title page, the §7.4 release and supplementary-record sentences, and the Appendix C archive and provenance lines. `ZENODO_DOI` is replaced at build time.

`header.tex` reproduces the original typesetting: fonts, colours, geometry, headings and captions. It was reconstructed from the published 8 October PDF, because the original style file was not part of the record. The two figures in `assets/` were cropped as unmodified vector regions from pages 7 and 8 of that PDF; they are the archived figures, not re-plots. Line breaks on pages 1–3 differ slightly from the 8 October PDF. Every table, figure and subsection keeps its page; the §4 and §6 headings, which sat alone at the foot of pages 4 and 6, now open the following page.

Build: `./build.sh` makes a watermarked preview; `./build.sh 10.5281/zenodo.NNNN` makes the release version. The build stops on missing glyphs or an unsubstituted DOI, and it verifies the 8 October files by hash before keeping copies in `downloads/archive/`.
