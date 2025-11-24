# Common Errors and Quick Fixes

- Fetch failures: check network/proxy; try `bitbake <target> -c fetch -f`; set mirrors if corporate network blocks git.
- Checksum mismatch: update `LIC_FILES_CHKSUM` or `SRC_URI[md5/sha256]` only after verifying the source change is expected.
- Missing dependencies: add build-time deps to `DEPENDS`, runtime to `RDEPENDS:${PN}`; rerun `bitbake-layers show-recipes <pkg>` to confirm providers.
- Disk space: clean with `bitbake -c cleansstate <recipe>` or prune old builds; keep `TMPDIR` on SSD with >100 GB free.
- Locale/encoding issues: ensure `LANG`/`LC_ALL` are UTF-8.
- Python errors in tasks: inspect `log.do_*` in `tmp/work/.../temp/`, re-run with `-DDD` for verbose python trace.
