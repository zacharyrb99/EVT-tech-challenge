FROM ubuntu:20.04 as builder
COPY . .
RUN apt-get update && apt-get install -y curl && ./docker_script.sh

FROM nginx:1.19.8
COPY --from=builder index.html /usr/share/nginx/html
COPY --from=builder certs/ /etc/nginx/certs
COPY nginx.conf /etc/nginx/conf.d/default.conf