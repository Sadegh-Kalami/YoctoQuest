# bbappend Files

- Naming: `<recipe>_<version>.bbappend` (version must match the target recipe or use `%` wildcard).
- Placement: same path structure as the original recipe inside your layer.
- Use `FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"` if you add patches/files.
- Common tweaks:
  - `SRC_URI:append = " file://fix.patch"`
  - `EXTRA_OECONF:append = " --enable-foo"`
  - `do_install:append()` to drop extra files.
- Verify with `bitbake-layers show-appends` and inspect the task logs to ensure your changes applied.
