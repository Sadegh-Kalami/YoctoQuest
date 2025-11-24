# First Build

From inside your initialized build directory (`build-yoctoquest`):

```bash
bitbake-layers show-layers        # sanity check
bitbake core-image-minimal        # first full build
```

Tips:
- Use parallelism: set `BB_NUMBER_THREADS ?= "${@oe.utils.cpu_count()}"` and `PARALLEL_MAKE ?= "-j ${@oe.utils.cpu_count()}"` in `local.conf`.
- Logs live under `tmp/log/` and per-task logs under `tmp/work/.../temp/log.*`.
- On failure, rerun with `-k` to keep going or inspect `log.do_compile`/`log.do_fetch` for errors.
- Record build time, cache sizes, and any fixes in `notes/learning-journal.md`.
