"""Configuration of the Google Wallet issuance profile.

Everything that differs between deployments arrives from the environment,
prefixed with ``EDUTAP_WALLET_GOOGLE_IDENTITY_``. Nothing is read from a
checked-in file.
"""

from pathlib import Path
from pydantic import AnyHttpUrl
from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


ENV_PREFIX = "EDUTAP_WALLET_GOOGLE_IDENTITY_"

#: URI scheme a wallet registers for Credential Offers.
#: OpenID4VCI 1.0, Section 4.
OFFER_URI_SCHEME = "openid-credential-offer://"


class Settings(BaseSettings):
    """Settings of the Google Wallet issuance profile."""

    model_config = SettingsConfigDict(
        env_prefix=ENV_PREFIX,
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    credential_issuer: AnyHttpUrl = Field(
        description=(
            "Our own Credential Issuer identifier. A wallet appends "
            "/.well-known/openid-credential-issuer to it to discover us, so it "
            "must be the public URL and not an internal one."
        ),
    )

    offer_uri_scheme: str = Field(
        default=OFFER_URI_SCHEME,
        description=(
            "Scheme used to hand a Credential Offer to the wallet application. "
            "Overridable because ecosystems register their own scheme."
        ),
    )

    trust_anchor_directory: Path | None = Field(
        default=None,
        description=(
            "Directory holding the issuing authority certificates a verifier "
            "chains against. Optional: a deployment that issues only SD-JWT VC "
            "needs no IACA."
        ),
    )
