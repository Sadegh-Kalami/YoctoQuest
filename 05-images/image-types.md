# Image Types

Common Yocto image recipes:
- `core-image-minimal`: smallest functional rootfs (baseline target for learning).
- `core-image-base`: adds common utilities and package management.
- `core-image-full-cmdline`: larger CLI environment.
- `core-image-x11`/`sato`: GUI targets (heavier, good for graphics testing).

Output artifacts (vary by machine):
- Rootfs: `.tar`, `.ext4`, `.wic`, `.sdimg`, `.rootfs.rpm/ipk/deb` feeds.
- Kernel: `zImage`, `Image`, `uImage` plus device trees (`.dtb`).
- Bootloader: `u-boot.bin`, SPL, or GRUB configs depending on BSP.

Use `bitbake -e <image> | grep ^IMAGE_FSTYPES` to see enabled formats.
