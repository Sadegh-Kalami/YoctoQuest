# Writing Recipes

Prereq: have a custom layer added to `BBLAYERS` (see `04-layers/creating-layers.md`).

1) Create a recipe directory, e.g., `meta-yoctoquest/recipes-example/hello/`.
2) Add `hello_0.1.bb`:
```bitbake
SUMMARY = "Tiny hello script"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=<md5>"
SRC_URI = "file://hello.sh"

S = "${WORKDIR}"
RDEPENDS:${PN} += "bash"

inherit allarch

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/hello.sh ${D}${bindir}/yoctoquest-hello
}
```
3) Add `hello.sh` next to the recipe:
```bash
#!/usr/bin/env bash
echo "Hello from YoctoQuest"
```
4) Build it: `bitbake hello`.
5) Add to an image: `IMAGE_INSTALL:append = " hello"` in your image recipe or `local.conf`.
6) Test inside the built image or SDK by running `yoctoquest-hello`.

Log steps and pitfalls in your journal; keep recipes minimal and focused.
