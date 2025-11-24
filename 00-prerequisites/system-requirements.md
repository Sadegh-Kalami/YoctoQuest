# System Requirements

Recommended host OS (desktop/server, 64-bit):
- Ubuntu 22.04/24.04 LTS, Debian 12, Fedora 39/40, openSUSE Leap/Tumbleweed, or CentOS Stream 9.
- Use WSL2 only if you must; avoid case-insensitive filesystems.

Hardware targets (per build machine):
- CPU: 8+ threads helps; 4 is workable for small builds.
- RAM: 16 GB minimum, 32 GB comfortable for kernels and SDKs.
- Disk: 100 GB free per build tree (downloads + sstate + tmp); use SSD/NVMe.

Other setup notes:
- Ensure `/bin/sh` is `bash` or `dash` (default on most distros).
- Set a UTF-8 locale (e.g., `en_US.UTF-8`).
- Stable internet access or internal mirrors for source downloads.
