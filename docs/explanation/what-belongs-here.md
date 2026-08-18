# About the boundary between this package and openid4vci

This package is small on purpose, and keeping it small takes a rule rather than good intentions.

## The rule

The protocol lives in `openid4vci`.
What a particular wallet does differently lives here.
The dependency points one way and never back: `openid4vci` must never learn that Google exists.

The test for a new piece of code is a question.
Would this be true if Google Wallet did not exist?
If yes, it belongs in `openid4vci`, even when Google is the reason you noticed it.

## What that leaves here

Three things survive the question.

The first is offer delivery.
A Credential Offer is standard, but how it reaches the wallet application is not: a deep link, a QR code, a platform-specific button.
This is the direct descendant of `api.save_link()` in `edutap.wallet_google`, one protocol generation later.

The second is the metadata profile.
Standard OpenID4VCI lets an issuer advertise whatever it can issue, and lets a wallet pick what it understands.
A given wallet therefore accepts a subset.
Google says publicly that Google Wallet supports `mso_mdoc` natively, and describes its infrastructure as format agnostic across W3C Verifiable Credentials and IETF SD-JWT VC.
Beyond that, the profile is not published, so it grows here as onboarding teaches it.

The third is trust anchors.
An ISO mdoc is accepted only if it chains to a registered issuing authority certificate, and which authorities a wallet trusts is the wallet's decision.

## Why the rule is worth defending

Vendor-specific code has a way of spreading.
It arrives as one conditional in a shared module, because that is where it is smallest, and by the time a second vendor appears the shared module is no longer shared.

Keeping the boundary at package level makes the spread visible: a Google-specific line in `openid4vci` requires a new import, and a new import is something a reviewer sees.
