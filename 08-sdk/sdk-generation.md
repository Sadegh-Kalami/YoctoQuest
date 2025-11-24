# SDK Generation

Build an SDK for your image:
```bash
bitbake core-image-minimal -c populate_sdk          # standard SDK
bitbake core-image-minimal -c populate_sdk_ext      # extensible SDK (preferred)
```

Install:
```bash
./tmp/deploy/sdk/poky-glibc-x86_64-core-image-minimal-*.sh
source /opt/poky/*/environment-setup-*
```

Notes:
- Use the eSDK when you need to add recipes or rebuild packages without the full build tree.
- Add host tools you need via `TOOLCHAIN_HOST_TASK`/`TOOLCHAIN_TARGET_TASK` in an SDK config or image recipe.
- Validate by building and running a small app with `devtool` inside the SDK.
