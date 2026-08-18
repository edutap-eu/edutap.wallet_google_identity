# Settings

The `Settings` class in `edutap.wallet_google_identity.settings` reads its values from the environment.
Every variable is prefixed with `EDUTAP_WALLET_GOOGLE_IDENTITY_`.
Names are case insensitive.
Unknown variables are ignored.
Values are also read from a `.env` file in the working directory, if one exists.

## Fields

`credential_issuer`
:   Type: URL.
    Required.

    The Credential Issuer identifier.
    A wallet appends `/.well-known/openid-credential-issuer` to this value to discover the issuer, so you must set it to the public URL.
    An internal address makes the issuer undiscoverable.

    Environment variable: `EDUTAP_WALLET_GOOGLE_IDENTITY_CREDENTIAL_ISSUER`

`offer_uri_scheme`
:   Type: string.
    Default: `openid-credential-offer://`

    The URI scheme used to hand a Credential Offer to the wallet application.
    The default is the scheme defined in OpenID4VCI 1.0, Section 4.
    Override it when an ecosystem registers its own scheme.

    Environment variable: `EDUTAP_WALLET_GOOGLE_IDENTITY_OFFER_URI_SCHEME`

`trust_anchor_directory`
:   Type: filesystem path.
    Default: none.

    Directory holding the issuing authority certificates that a verifier chains against.
    You must set this when you issue `mso_mdoc` credentials.
    A deployment that issues only SD-JWT VC needs no issuing authority certificate and may leave it unset.

    Environment variable: `EDUTAP_WALLET_GOOGLE_IDENTITY_TRUST_ANCHOR_DIRECTORY`

## Example

```shell
export EDUTAP_WALLET_GOOGLE_IDENTITY_CREDENTIAL_ISSUER="https://wallet.example.edu/"
export EDUTAP_WALLET_GOOGLE_IDENTITY_TRUST_ANCHOR_DIRECTORY="/etc/edutap/trust"
```

```python
from edutap.wallet_google_identity.settings import Settings

settings = Settings()
```
