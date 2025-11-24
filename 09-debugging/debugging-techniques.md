# Debugging Techniques

- Inspect tasks: `bitbake -c listtasks <recipe>`, `bitbake -c cleansstate <recipe>`, and rerun the failing task.
- Environment dumps: `bitbake -e <recipe> | less` to see final variable values; use `/^VAR=` searches.
- Dependency graph: `bitbake -g <image>` to emit `pn-depends.dot`; view with `xdot` or `dot -Tsvg`.
- Drop into a shell: `bitbake -c devshell <recipe>` for a preconfigured build shell.
- Runtime debugging: use `strace`, `gdb`, or `systemd-analyze` inside the target; ensure debug symbols with `EXTRA_IMAGE_FEATURES += " dbg-pkgs"` when needed.
- Logging: check `tmp/log/` for global logs; per-task logs live in `tmp/work/.../temp/`.
