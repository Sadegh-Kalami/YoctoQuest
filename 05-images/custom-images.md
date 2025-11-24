# Custom Images

Create your own image recipe in your layer (e.g., `recipes-core/images/yoctoquest-image.bb`):
```bitbake
SUMMARY = "YoctoQuest image"
LICENSE = "MIT"
require recipes-core/images/core-image-base.bb

IMAGE_INSTALL:append = " hello openssh"
IMAGE_FEATURES:append = " ssh-server-openssh package-management"
```

Build and inspect:
```bash
bitbake yoctoquest-image
ls tmp/deploy/images/${MACHINE}/
```

Tips:
- Reuse `core-image-minimal` or `core-image-base` via `require` to avoid duplication.
- Add packagegroups for groups of apps rather than many single packages.
- Keep `IMAGE_FEATURES` lean; enable debug options only when investigating issues.
- Document every image variant you keep; prune old ones to avoid confusion.
