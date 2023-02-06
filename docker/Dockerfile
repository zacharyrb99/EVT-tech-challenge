FROM ubuntu:20.04 as builder
COPY . .
RUN apt-get update && apt-get install -y curl && curl https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html >> index.html

FROM nginx:1.19.8
COPY --from=builder index.html /usr/share/nginx/html
COPY --from=builder certs/ /etc/nginx/certs
COPY nginx.conf /etc/nginx/conf.d/default.conf