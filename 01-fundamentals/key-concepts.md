# Key Concepts

- Recipe (`.bb`): metadata describing how to fetch, configure, build, and package one component.
- Class (`.bbclass`): reusable functions/macros that recipes inherit (e.g., `autotools`, `cmake`).
- Layer: collection of recipes and configs with clear scope; stacked via `BBLAYERS`.
- Machine: board-specific settings (tuning, kernel, bootloader) selected by `MACHINE`.
- Distro: policy choices (init system, package format, branding) selected by `DISTRO`.
- Image: rootfs definition built from package/packagegroup lists and feature flags.
- Task: unit of work in BitBake (`do_fetch`, `do_compile`, `do_install`, `do_rootfs`).
- bbappend (`.bbappend`): file that extends/overrides a recipe from another layer.
- Feeds: package repositories (`ipk`, `rpm`, `deb`) generated from built packages.
