# Recipe Syntax Quick Notes

Minimal fields you almost always set:
- `SUMMARY`, `DESCRIPTION`, `HOMEPAGE`, `LICENSE`, `LIC_FILES_CHKSUM`.
- `SRC_URI` (supports `git://`, `https://`, `file://`); pin with `SRCREV` for git.
- `S` (source dir) and optionally `PV`/`PR` (version/revision).
- `DEPENDS` for build-time deps; `RDEPENDS:${PN}` for runtime deps.
- `inherit` common classes (`autotools`, `cmake`, `python_setuptools_build_meta`, `packagegroup`).

Common tasks (override with `do_<task>()`): `do_fetch`, `do_unpack`, `do_patch`, `do_configure`, `do_compile`, `do_install`, `do_package`, `do_rootfs`.

Example skeleton:
```bitbake
SUMMARY = "Hello example"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=<md5>"
SRC_URI = "git://github.com/example/hello.git;branch=main"
SRCREV = "<commit>"
S = "${WORKDIR}/git"

inherit cmake

EXTRA_OECMAKE += "-DENABLE_FOO=ON"

RDEPENDS:${PN} += "bash"
FILES:${PN} += "${bindir}/hello"
```
