# player-api

For handling player actions.

## Overview

### GET

#### Creat new player

`curl "http://<host>/v0

**Response**

## Development

Test against your local `MySQL` instance. See the `game-database` repository
for latest database schema and test data. The username and password needed for
you database is in the `Makefile`. Don't forget to give your database user full
privileges or you may have trouble running the tests.

## Docker

> docker build -t player-api .

You only need to build this image if you are working on the `game-service`
repository.
