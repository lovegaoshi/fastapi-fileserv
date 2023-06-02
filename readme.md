# Vercel Deployment of NoxBackup

This is a vercel version of a simple data serving server written in fastapi, for cloud sync of noxplayer.

To deploy, connect a postgresSQL vercel database to this project; and configure these two additional environment variables:

`POSTGRES_HOST`: the port of the postgreSQL access URI

`USERID`: user ids to authenticate, can be multiple, joined by a single comma.
