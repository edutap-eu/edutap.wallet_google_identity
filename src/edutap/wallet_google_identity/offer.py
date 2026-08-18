"""Delivering a Credential Offer to Google Wallet.

The Credential Offer itself is standard (OpenID4VCI 1.0, Section 4). What
differs per platform is how the offer reaches the wallet application: as a
deep link the user taps, or as a QR code they scan.

This module is the counterpart of ``api.save_link()`` in ``edutap.wallet_google``
-- the same idea, one protocol generation later.
"""
