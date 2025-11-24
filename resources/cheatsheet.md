# Cheatsheet

- Init build env: `source oe-init-build-env build-yoctoquest`
- Show layers: `bitbake-layers show-layers`
- List recipes: `bitbake-layers show-recipes <pattern>`
- Build image: `bitbake core-image-minimal`
- Clean and rebuild recipe: `bitbake -c cleansstate <recipe> && bitbake <recipe>`
- Inspect vars: `bitbake -e <recipe> | less`
- Add layer: `bitbake-layers add-layer ../meta-<name>`
- Generate SDK: `bitbake <image> -c populate_sdk_ext`
- Serve feeds: `python3 -m http.server 8080` from `tmp/deploy/<pkgformat>`
