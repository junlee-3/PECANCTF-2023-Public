# Great Tor Reveal 2

Important things to note.

Same as last time!

The container will create a random .onion address and output it to the log (viewable with `docker-compose logs`). This is the target that students will need to attack to find the real domain.

## tl;dr

/server-status endpoint revealing flag in http request.

PoC:

```bash
curl -vv --socks4a 127.0.0.1:9050 something.onion/server-status
```
