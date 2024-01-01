#!/bin/sh
chown -R $(id -u):$(id -g) /opt/mindustry/config
cd /opt/mindustry
su -s '/bin/sh' $(id -u) -c "java -jar -Xmx$JVM_XMX -Xms$JVM_XMS /opt/mindustry/server-release.jar"
