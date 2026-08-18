# edutap.wallet_google_identity

**Google Wallet profile for OpenID for Verifiable Credential Issuance.**

Google accepts two integration protocols for issuing digital credentials into
Google Wallet: its own Digital Credentials Provisioning API, or OpenID4VCI.
This package takes the OpenID4VCI route. The protocol lives in
`openid4vci`; only what is specific to
Google lives here.

> **Pre-alpha.** Configuration is implemented, issuance is not.

## What belongs here

The dependency points one way and never back — `openid4vci` must never learn
that Google exists. The test for new code is a question: *would this be true if
Google Wallet did not exist?* If yes, it belongs in `openid4vci`.

Three things survive that question:

| Module | Purpose |
| --- | --- |
| `offer.py` | How a Credential Offer reaches the wallet — deep link, QR code, button |
| `models/metadata.py` | The subset of `credential_configurations_supported` Google Wallet accepts |
| `trust.py` | Issuing authority certificates an mdoc chains against |

## Installation

`openid4vci` is not on PyPI yet. Inside the eduTAP development setup both
packages sit side by side and `[tool.uv.sources]` resolves it from there:

```shell
uv sync --group test
make test-local
```

See the [how-to guide](docs/how-to/install-for-development.md) for the details.

## Documentation

The documentation follows [Diataxis](https://diataxis.fr/) and builds with
Sphinx and MyST:

```shell
make docs
```

Start with [About the choice of OpenID4VCI](docs/explanation/why-openid4vci.md)
for why this package exists at all.

## License

[EUPL 1.2](https://opensource.org/license/eupl-1-2/)
