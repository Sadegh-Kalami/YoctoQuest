# Package Management

- Choose a package format in `local.conf` or distro config: `PACKAGE_CLASSES = "package_ipk"` (or `package_rpm`, `package_deb`).
- Enable package management in images: `IMAGE_FEATURES:append = " package-management"`.
- Generate feeds during build: `bitbake <image>` produces `*-deploy/ipk|rpm|deb` repos under `tmp/deploy/<format>/`.
- Serve feeds via simple HTTP for testing: `python3 -m http.server 8080` from the deploy dir.
- For custom packagegroups, create a recipe inheriting `packagegroup` and list packages in `RDEPENDS:${PN}`.
