# Flask-Tus-Ponthe
This is a fork of [matthoskins1980's implementation of the tus protocol for flask](https://github.com/matthoskins1980/Flask-Tus).

## Redis (instructions on Archlinux)

Need for a Redis server on default port 6379 :
```
sudo pacman -S redis
sudo systemctl start redis
```

Connect to Redis CLI :
```
redis-cli
```

Empty database :
```
FLUSHALL
```

Show existing keys (default database is index 0):
```
SELECT 0
KEYS *
```
ou
```
SELECT 0
SCAN 0
``
