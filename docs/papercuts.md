# Papercuts

## 2026-08-25: Anki sync validation missed a stale variable

The worker-thread change in `push_to_anki.py` stored the sync status in `required`, but the output still referenced the removed `result` variable. The dry run did not execute the sync path, so it did not detect the error. A local fake `Collection` was used to exercise `do_sync()` without contacting AnkiWeb
