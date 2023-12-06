# Utiliser l'image MySQL officielle comme base
FROM mysql:latest

# Copier les scripts SQL dans le conteneur
COPY ./SCHEMA.sql /docker-entrypoint-initdb.d/1_SCHEMA.sql
COPY ./PRIVILEGES.sql /docker-entrypoint-initdb.d/2_PRIVILEGES.sql
