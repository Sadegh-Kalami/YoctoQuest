# Kernel Customization

- Prefer kernel recipes from your BSP layer; avoid editing vendor sources directly.
- Add config fragments via `SRC_URI += "file://myfragment.cfg"` and set `KERNEL_FEATURES:append = " cfg/myfragment.cfg"` if using KSP.
- Run `bitbake -c menuconfig virtual/kernel` for quick tweaks; commit generated fragments to your layer, not the workdir.
- Apply patches with `SRC_URI:append = " file://fix.patch"`; keep them minimal and upstreamable.
- Rebuild with `bitbake -c cleansstate virtual/kernel && bitbake <image>` when changing kernel sources/config.
