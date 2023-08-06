# The Great Tor Reveal 1

Important things to note.

The container will create a random .onion address and output it to the log (viewable with `docker-compose logs`). This is the target that students will need to attack to find the real domain.

## tl;dr

HTTP/1.0 downgrade without hostname header to error page reveals default apache hostname.

PoC:

```bash
curl -vv -0 -H "Host:" --socks4a 127.0.0.1:9050 something.onion/
```
