# Glossary (quick lookup)

- BitBake: task executor and build tool used by Yocto.
- Poky: Yocto reference distro (BitBake + OE-Core + meta-poky/meta-yocto-bsp).
- Recipe: `.bb` file describing how to build and package one component.
- Layer: collection of recipes/configs grouped by purpose.
- Machine: board-specific configuration selected via `MACHINE`.
- Distro: policy configuration selected via `DISTRO`.
- Sstate: shared-state cache of task outputs.
- BBAPPEND: file that extends/overrides an existing recipe.
- Image: root filesystem definition built by BitBake.
- SDK/eSDK: cross-toolchain (standard) or extensible SDK for app/layer development.
