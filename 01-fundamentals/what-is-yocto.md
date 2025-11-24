# What Is the Yocto Project?

- A set of tools and metadata to build custom, reproducible Linux distributions for embedded devices.
- Not a binary distro; you assemble your own using recipes, layers, and BitBake tasks.
- Poky is the reference distribution (BitBake + OE-Core + meta-poky and friends).
- Outputs include root filesystems, kernel images, bootloaders, SDKs, and package feeds.
- Typical alternatives: Buildroot (simpler, fewer knobs) and vendor BSPs (fast start, less control).
