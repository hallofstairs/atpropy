# atprotocol 

🚧 Under construction 🚧

Python 3.10 wrapper for the [ATProtocol API](https://github.com/bluesky-social/atproto/tree/main/packages/api). It aims to closely emulate the Typescript implementation, including:
- APIs for ATProtocol and Bluesky
- Validation and (almost) complete types

## Getting started

First install the package:

```shell
pip install atprotocol
```

Then in your application:

```python
from atprotocol.bsky import BskyAgent

agent = BskyAgent()
```

## Usage

### Session management
Log into a server using these APIs. You'll need an active session for most methods.

```python
from atprotocol.bsky import BskyAgent

agent = BskyAgent()
agent.login(identifier='jett.ai', password='letsgoduke')
```

### API calls

These are the calls currently available in `atprotocol`. More are being added regularly.

```python
# Feeds and content
agent.get_timeline()
agent.get_author_feed(actor, limit)
agent.get_post_thread(uri, depth)
agent.get_likes(uri, cid, limit)
agent.get_reposted_by(uri, cid, limit)

# Social graph
agent.get_followers(actor)

# Actors
agent.get_profile(actor)
agent.get_profiles(actors)
agent.search_actors(term, limit)

# Session management
agent.login(params)
```

## Advanced

### Generic agent

If you want a generic AT Protocol agent without methods related to the Bluesky social lexicon, use the AtpAgent instead of the BskyAgent.

```python
from atprotocol import AtpAgent

agent = AtpAgent(service='https://example.com')
```


## License
MIT