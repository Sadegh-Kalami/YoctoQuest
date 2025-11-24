# Poky Setup

Use a clean workspace outside this repo, e.g., `~/yocto-build`.

```bash
mkdir -p ~/yocto-build
cd ~/yocto-build
git clone git://git.yoctoproject.org/poky -b scarthgap
cd poky
source oe-init-build-env build-yoctoquest
```

Notes:
- `oe-init-build-env` creates `conf/`, sets `BBPATH`, and drops you into the build dir.
- Set shared caches once in `conf/local.conf` to speed rebuilds and share across projects:
  ```
  DL_DIR ?= "/home/$USER/yocto-downloads"
  SSTATE_DIR ?= "/home/$USER/yocto-sstate"
  TMPDIR ?= "${TOPDIR}/tmp"
  ```
- Keep the poky clone clean; use separate layers for changes.
