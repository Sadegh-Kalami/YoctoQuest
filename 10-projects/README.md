# 10 - Projects

Use this area for hands-on exercises. Suggested layout:
- `project-<name>/README.md` describing goals, hardware, and target image.
- `project-<name>/tasks.md` with a short checklist.
- Keep build artifacts out of the repo; point to the external build dir you used.

Starter ideas:
- Build `core-image-minimal` for QEMU and boot it.
- Create a custom packagegroup and image that uses it.
- Add a simple systemd service and verify it starts on boot.
- Generate an eSDK and build an app with `devtool`.
