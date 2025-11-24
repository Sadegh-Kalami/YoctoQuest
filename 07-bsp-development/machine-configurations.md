# Machine Configurations

Machine configs live in `conf/machine/<machine>.conf` inside a BSP layer.

Key variables:
- `MACHINEOVERRIDES`/`DEFAULTTUNE`: CPU tuning and overrides.
- `PREFERRED_PROVIDER_virtual/kernel`, `KERNEL_IMAGETYPE`, `KERNEL_DEVICETREE`.
- `UBOOT_MACHINE` or other bootloader settings.
- `IMAGE_FSTYPES`: formats to emit for this board (e.g., `wic.bz2`, `sdimg`).
- `SERIAL_CONSOLE`: console device/baud for login.
- `WKS_FILE`: wic kickstart file for image layout when needed.

Test flow:
1) Start from vendor BSP layer; add a small overlay layer for changes.
2) Build a minimal image for the machine; boot it in QEMU or on hardware.
3) Capture boot logs and tweaks in your journal.
