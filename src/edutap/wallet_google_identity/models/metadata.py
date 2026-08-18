"""The Google Wallet profile of the Credential Issuer Metadata.

Standard OpenID4VCI leaves ``credential_configurations_supported`` open: an
issuer advertises whatever it can issue, and a wallet picks what it
understands. A given wallet therefore accepts a subset, and this module
describes Google's.

What is documented publicly today is thin -- Google Wallet supports
``mso_mdoc`` natively (for example ``org.iso.18013.5.1.mDL``) and describes
its infrastructure as format agnostic, covering W3C Verifiable Credentials
and IETF SD-JWT VC. Anything beyond that comes from the issuer onboarding, so
this profile grows as we learn it rather than being guessed up front.
"""
