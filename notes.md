# ATP Overview

## Data management

- A data repository (repo) is the dataset of a single "user" in the ATP network
- Every user has a single repo which is identified by a [DID](https://w3c.github.io/did-core/)
  - DIDs strongly identify repos
  - Handles can be used, but DID is preferred
  - You can resolve a handle to a DID with [`com.atproto.identity.resolveHandle`](https://atproto.com/lexicons/com-atproto-identity#comatprotoidentityresolvehandle)
- Repos are composed of collections, which are ordered lists of records. Each collection is identified by an [NSID](https://atproto.com/specs/nsid), eg `app.bsky.feed.post` contains all of a user's posts on Bluesky
  - Collections only contain records of the type identified by their NSID
- A record is a key/value document. It's the smallest unit of data which can be transmitted over the network. Every record has a type and is identified by a [TID](https://atproto.com/specs/atp#timestamp-ids-tid)


## Federation

- Personal data servers house repos


## Random

- Any verified user can view the repo of any other user
  - I think this is generally true, I *know* it's true for users on the same server eg bsky.social

- You access collections within a repo by performing a GET request on <SERVER>/<COLLECTION>