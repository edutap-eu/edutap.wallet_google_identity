# How to install the package for development

This guide shows you how to get the package running on your machine.

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
