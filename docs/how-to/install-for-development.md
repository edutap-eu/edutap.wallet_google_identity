# How to install the package for development

This guide shows you how to get the package running on your machine, including its unreleased dependency.

## Resolve the OpenID4VCI dependency

This package depends on `openid4vci`, which is not published to PyPI yet.
Inside the eduTAP development setup both packages sit side by side under `uses_libraries/`, and `pyproject.toml` resolves the dependency from there:

```toml
[tool.uv.sources]
openid4vci = { path = "../OpenID4VCI", editable = true }
```

If you check out this package on its own, clone `openid4vci` next to it, or point that path at wherever you keep it.

```{important}
The `[tool.uv.sources]` section is development metadata.
It is not part of the published wheel, so it never reaches anyone installing the package from an index.
```

## Install and run the tests

```shell
uv sync --group test
uv run pytest
```

Or through the Makefile, which is the same set of entry points every eduTAP package offers:

```shell
make test-local
make lint
make typecheck
```

## Build the documentation

```shell
make docs
```

The build treats warnings as errors, so a broken cross-reference fails the build rather than shipping.
To check that every external link still resolves:

```shell
make docs-linkcheck
```

While writing, use the autoreloading build instead:

```shell
make docs-live
```
