# Build Directory Structure

Key paths after running `oe-init-build-env` and building:
- `conf/`: `local.conf`, `bblayers.conf`, site/mirror overrides.
- `downloads/`: source tarballs and git mirrors (keep outside repo, shareable).
- `sstate-cache/`: task artifacts for fast rebuilds (share between builds when possible).
- `tmp/`: build output tree; contains workdirs, sysroots, and deploy artifacts.
- `tmp/work/<arch>/<recipe>/temp/`: per-task logs and runfiles.
- `tmp/deploy/images/<machine>/`: kernel, bootloader, and rootfs images.
- `tmp/deploy/sdk/`: generated SDK installers.
- `cache/` and `bitbake-cookerdaemon.log`: BitBake parser cache and daemon log.
