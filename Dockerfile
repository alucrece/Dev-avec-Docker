FROM postgres:16-alpine3.22

COPY ./sqlfiles/migration-v001.sql /docker-entrypoint-initdb.d/

EXPOSE 5432