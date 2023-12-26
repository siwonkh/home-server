#!/bin/sh
chown -R mindustry:mindustry /opt/mindustry/config
cd /opt/mindustry
su -s '/bin/sh' mindustry -c "java -jar -Xmx$JVM_XMX -Xms$JVM_XMS /opt/mindustry/server-release.jar"