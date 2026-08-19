# edutap.wallet_google_identity

Google Wallet profile for OpenID for Verifiable Credential Issuance.

Google accepts two integration protocols for issuing digital credentials into Google Wallet: its own Digital Credentials Provisioning API, or OpenID4VCI.
This package takes the OpenID4VCI route.
The protocol itself lives in the [openid4vci](https://github.com/edutap-eu/OpenID4VCI) package, and only what is specific to Google lives here.

```{warning}
This package is pre-alpha.
Configuration is implemented; issuance is not.
Read {doc}`explanation/why-openid4vci` for where the boundary runs and why.
```

```{toctree}
:maxdepth: 2

tutorials/index
how-to/index
reference/index
explanation/index
```
