FROM alpine

ARG TAG_NAME=v146
ENV CONFIG=/opt/mindustry/config

RUN \
    apk add --no-cache openjdk17-jre shadow  && \
    mkdir -p /opt/mindustry && \
    mkdir -p /opt/mindustry/config && \
    useradd -u 999 -U -s /bin/false mindustry && \
    groupmod -o -g 1000 mindustry && \
    usermod -G mindustry mindustry && \
    chown mindustry:mindustry -R /opt/mindustry/config && \
    wget https://github.com/Anuken/Mindustry/releases/download/${TAG_NAME}/server-release.jar -O /opt/mindustry/server-release.jar

EXPOSE 6567

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
