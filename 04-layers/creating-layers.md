# Creating Layers

From your build directory:
```bash
bitbake-layers create-layer ../meta-yoctoquest
bitbake-layers add-layer ../meta-yoctoquest
bitbake-layers show-layers
```

Tweak `meta-yoctoquest/conf/layer.conf`:
```
BBFILE_PRIORITY_meta-yoctoquest = "7"
LAYERSERIES_COMPAT_meta-yoctoquest = "scarthgap"
```

Guidelines:
- Keep recipes under `recipes-<domain>/...` and classes under `classes/`.
- Add layer dependencies in `LAYERDEPENDS` (e.g., `LAYERDEPENDS_meta-yoctoquest = "core"`).
- Avoid hardcoding absolute paths; rely on `${LAYERDIR}`.
- Version control your layer separately if it will be reused across projects.
