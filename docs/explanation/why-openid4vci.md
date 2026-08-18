# About the choice of OpenID4VCI

Google offers two ways to issue a digital credential into Google Wallet, and this package uses the second one.
The choice is worth recording, because from the outside the first one looks like the obvious path: it is the one Google documents in depth.

## The two integration paths

The [Digital Credentials Provisioning API](https://developers.google.com/wallet/identity/provisioning) is Google's own protocol.
It is documented thoroughly, down to endpoint lists and encryption formats, and it is built around ISO/IEC 18013-5.
Its shape is unusual: of its endpoints, most are hosted by the issuer, not by Google.
Google calls us, over mutual TLS, with a client certificate we are expected to pin.

The second path is OpenID4VCI.
Google states it plainly on [its identity overview](https://developers.google.com/wallet/identity/identity_frame): "Implement one of the supported integration protocols: Google Digital Credentials Provisioning API, or OpenID4VCI."
That single sentence is, as of today, close to everything Google says publicly about it.

## Why the sparsely documented path won

The asymmetry in documentation is real, and it argues for the proprietary API.
Three things argue louder for the standard.

The first is reuse.
An issuer that speaks OpenID4VCI speaks it to every wallet that speaks it, and the EUDI Wallet, Samsung Wallet and others do.
Effort spent on the standard is spent once.
Effort spent on the proprietary API is spent again for the next platform, and again for the one after that.

The second is where the work lands.
The proprietary path is substantially an operations problem rather than a library problem: mutual TLS with certificate pinning, Mobile Security Object release, an issuer-hosted surface that Google reaches into.
Certificate pinning in particular is a property of the deployment, not of a Python package, and it does not become simpler by being wrapped in one.

The third is the shape of the eventual system.
A university credential is not a driving licence.
The proprietary path is designed around the mDL case and carries its assumptions; the standard leaves the credential format open and lets an issuer serve `dc+sd-jwt` where selective disclosure matters more than ISO conformance.

## What this costs us

Honesty about the trade-off matters more than the decision.

The public documentation for Google's OpenID4VCI path is one sentence.
There is no published profile, no list of extension parameters, no worked example.
Whatever Google requires beyond the specification, we will learn during issuer onboarding rather than by reading.

That is why this package stays deliberately small, and why {doc}`what-belongs-here` draws the line where it does.
A thin package can absorb what onboarding teaches us.
A thick one, built on guesses about a profile nobody published, would have to be unbuilt first.

```{seealso}
The specification itself: [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html).
The interoperability profile that pins down formats and proof types: [OpenID4VC High Assurance Interoperability Profile 1.0](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0.html).
```
