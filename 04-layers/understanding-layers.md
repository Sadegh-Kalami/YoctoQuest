# Understanding Layers

- Layers group related metadata (recipes, classes, configs) with clear scope (BSP, distro, apps).
- `conf/layer.conf` sets `BBFILE_COLLECTIONS`, `BBFILE_PATTERN`, `BBFILE_PRIORITY`, `LAYERDEPENDS`, and `LAYERSERIES_COMPAT`.
- Priority resolves conflicts when the same recipe exists in multiple layers; keep priorities explicit.
- Keep vendor BSP layers separate from your app layers; avoid modifying poky/OE-Core directly.
- Use `bitbake-layers show-layers` and `bitbake-layers show-recipes` to inspect what BitBake sees.
