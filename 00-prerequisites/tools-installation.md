# Tools Installation

Install base Yocto host packages before cloning `poky`.

## Ubuntu / Debian (apt)
```bash
sudo apt-get update
sudo apt-get install -y \
  gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio \
  python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping \
  python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint bmap-tools \
  lz4 zstd
```

## Fedora (dnf)
```bash
sudo dnf groupinstall -y "Development Tools" "Development Libraries"
sudo dnf install -y \
  gawk wget git diffstat unzip texinfo chrpath socat cpio python3 python3-pip \
  python3-pexpect xz debianutils iputils python3-GitPython python3-jinja2 \
  mesa-libEGL-devel SDL-devel pylint bmap-tools lz4 zstd
```

## Post-install checks
- `git --version`, `python3 --version`, and `bitbake --version` (after you source `oe-init-build-env`).
- Add your user to `disk` groups as needed for external drives.
- Record any proxies/mirrors in your journal and export them in your shell profile if required.
