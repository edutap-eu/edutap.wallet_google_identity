from edutap.wallet_google_identity.settings import Settings
from pydantic import ValidationError

import pytest


def test_credential_issuer_is_required():
    """Without an issuer identifier there is nothing to point a Wallet at."""
    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_offer_uri_scheme_defaults_to_the_registered_scheme():
    settings = Settings(
        _env_file=None,
        credential_issuer="https://wallet.example.edu/",
    )
    assert settings.offer_uri_scheme == "openid-credential-offer://"


def test_settings_read_the_environment_with_the_package_prefix(monkeypatch):
    monkeypatch.setenv(
        "EDUTAP_WALLET_GOOGLE_IDENTITY_CREDENTIAL_ISSUER",
        "https://wallet.example.edu/",
    )
    monkeypatch.setenv(
        "EDUTAP_WALLET_GOOGLE_IDENTITY_OFFER_URI_SCHEME",
        "haip://",
    )

    settings = Settings(_env_file=None)

    assert str(settings.credential_issuer) == "https://wallet.example.edu/"
    assert settings.offer_uri_scheme == "haip://"


def test_trust_anchor_directory_is_optional():
    settings = Settings(
        _env_file=None,
        credential_issuer="https://wallet.example.edu/",
    )
    assert settings.trust_anchor_directory is None
