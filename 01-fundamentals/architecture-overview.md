# Architecture Overview

- BitBake parses recipes (`.bb`) and classes (`.bbclass`), resolves dependencies, and schedules tasks.
- Metadata comes from layers stacked via `bblayers.conf` (e.g., poky, meta-openembedded, vendor BSPs).
- OE-Core supplies the core classes, functions, and base recipes; Poky bundles BitBake + OE-Core + reference layers.
- Sstate cache stores task outputs to speed rebuilds; downloads cache source tarballs.
- Configuration flows: distro config → machine config → layer/app overrides → local.conf tweaks.
