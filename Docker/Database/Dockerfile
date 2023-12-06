# Utiliser l'image MySQL officielle comme base
FROM mysql:8.1.0

ENV MYSQL_ROOT_PASSWORD=root_password

# Copier les scripts SQL dans le conteneur
COPY ./SCHEMA.sql /docker-entrypoint-initdb.d/1_SCHEMA.sql
COPY ./PRIVILEGES.sql /docker-entrypoint-initdb.d/2_PRIVILEGES.sql
