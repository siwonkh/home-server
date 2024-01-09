FROM caddy:builder-alpine AS builder
RUN xcaddy build

FROM caddy:alpine as runtime
COPY --from=builder /usr/bin/caddy /usr/bin/caddy