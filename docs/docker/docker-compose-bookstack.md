---
title: "docker-compose - bookstack"
date: 2025-09-13T17:37:46.000Z
slug: docker-compose-bookstack
---

``` yaml
services:
  bookstack:
    image: lscr.io/linuxserver/bookstack
    container_name: bookstack
    environment:
      - PUID=1000
      - PGID=1000
      - APP_URL=https://nombre.dominio.com
      - DB_HOST=bookstack_db
      - DB_PORT=3306
      - DB_USER=bookstack
      - DB_PASS=7VJccQxL8
      - DB_DATABASE=bookstackapp
      - APP_DEFAULT_DARK_MODE=true
      - APP_AUTO_LANG_PUBLIC==false
      - APP_LANG=es
    volumes:
      - ./bookstack/app_data:/config
    ports:
      - 3075:80
    restart: unless-stopped
    depends_on:
      - bookstack_db
  bookstack_db:
    image: lscr.io/linuxserver/mariadb
    container_name: bookstack_db
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_ROOT_PASSWORD=oiXCMEB5r
      - TZ=America/Panama
      - MYSQL_DATABASE=bookstackapp
      - MYSQL_USER=bookstack
      - MYSQL_PASSWORD=7VJccQxL8
    volumes:
      - ./bookstack/db_data:/config
    restart: unless-stopped
```
