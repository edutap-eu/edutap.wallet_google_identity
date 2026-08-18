"""Trust anchors for credentials issued into Google Wallet.

An ISO mdoc is only accepted by a verifier if it chains to a trusted issuing
authority certificate (IACA), and the document signer certificate under it is
what actually signs the Mobile Security Object.

Neither is ours to invent: the trust anchor is registered with the ecosystem,
and Google publishes the list of issuers it accepts. This module holds the
loading and validation, not the keys.
"""
