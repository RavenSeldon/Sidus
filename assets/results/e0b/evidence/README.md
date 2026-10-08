# E0-B MB0–MB2 archive (8 October 2026)

Requirements: Python 3.11+, numpy, scipy. Run from this directory.

| Order | Command | Log | Approx. time |
|---|---|---|---|
| 1 | `python3 e0b_mb0.py` | mb0_output.md | 1–2 min |
| 2 | `python3 e0b_mb12.py` | mb12_output.md | ~25 min |
| 3 | `python3 e0b_mb2_diag.py` | mb2_diag_output.md | ~5 min |
| 4 | `python3 e0b_mb2_diag2.py` | mb2_diag2_output.md | ~15 min |
| 5 | `python3 e0b_mb1_lsq.py` | mb1_lsq_output.md | seconds |
| 6 | `python3 e0b_power.py` | power_output.md | ~10 min (fixed seed 20261008) |
| — | earlier: e0b_reference.py, e0b_contracts.py, e0b_shea_repair.py, e0b_r24.py | contract_output.md, shea_repair_output.txt | — |

Note: the RR1c line in mb12_output.md reflects ONE admissible consumer (the LP solver's). It is superseded by the identification analysis in mb2_diag_output.md (X1), as recorded in the Final-State Report §4.4.

## v2 additions (Ledger E, 8 October 2026)

| Order | Command | Log | Approx. time |
|---|---|---|---|
| 7 | `python3 e0b_ledgerE.py` | ledgerE_output.md | ~10 min |
| 8 | `python3 e0b_ledgerE_s1e.py` | ledgerE_s1e_output.md | seconds |
| 9 | `python3 e0b_assert.py` | assert_output.md, ENVIRONMENT.txt | ~30 s (exits non-zero on any failed assertion) |

Archive v1 (`E0B_MB0-MB2_archive.zip`) is preserved unchanged; this v2 supersedes it only by addition.

## v3 additions (Ledger F + Learned Pilot P0, 8 October 2026)

| Order | Command | Log | Approx. time |
|---|---|---|---|
| 10 | `python3 e0b_ledgerF.py` | ledgerF_output.md | ~10 min |
| 11 | `python3 e0b_assert_v2.py --full` | assert_v2_output.md | ~9 min (43 assertions) |
| 12 | `python3 e0b_pilot.py all 10` | pilot_output.md, pilot_*_results.json, pilot_trials/ | ~15 min (pilot seeds 1-10 only) |
| 13 | `python3 e0b_pilot_analysis.py` | pilot_analysis.md | seconds (applies the pre-committed rules) |
| 14 | `python3 e0b_pilot_process_check.py` | pilot_process_check.md | seconds (exact) |
| 15 | `python3 e0b_process_family_probe.py` | process_family_probe.md | ~1 min (exploratory) |

Pilot protocol `E0B_Pilot_Protocol_P0.md` was committed by SHA-256 before any pilot run (pilot_protocol_commitment.txt). Confirmation seeds 1001+ have never been used.

## v4 additions (Ledger G, freeze, confirmation — 8 October 2026)

| Order | Command | Log | Approx. time |
|---|---|---|---|
| 16 | `python3 e0b_confirm.py recheck` | recheck_output.md, recheck_results.json, recheck_thresholds.json | ~15 min (pilot seeds 1-10, exploratory) |
| 17 | `python3 e0b_confirm.py confirm` | confirm_output.md, confirm_results.json, confirm_adjudication.json | ~25 min (seeds 1001-1020; requires E0B_Frozen_Confirmation_Spec.json) |

Governance order: confirmation rules committed (confirmation_rules_commitment.txt) -> recheck -> freeze (freeze_commitment.txt) -> confirmation. See E0B_Closing_Report.md section 2.
