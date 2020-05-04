#!/usr/bin/env bash

set -x

set -eo pipefail

REPO_DIR=git_repos
PROJ_DIR=batch_tabs

cd ${HOME}/${REPO_DIR}

# git pull

if [[ -d ${HOME}/${PROJ_DIR} ]]; then
    rm -rf ${HOME}/${PROJ_DIR}
fi

cp -R ${PROJ_DIR} ${HOME}

if [[ ! -d '/etc/letsencrypt/' ]]; then
    . ${HOME}/ssl_request.sh
else
    sudo cp -R /etc/letsencrypt/ ${HOME}/${PROJ_DIR}
    sudo chown -R $USER:$USER ${HOME}/${PROJ_DIR}/letsencrypt
fi

cp ${HOME}/bt_secret/* ${HOME}/${PROJ_DIR}/src/bt/

cd ${HOME}/${PROJ_DIR}/docker

if [[ $1 = 'local' ]]; then
    mv docker-compose.yml docker-compose-static-nginx.yml
    mv docker-compose-static-local.yml docker-compose.yml
fi

cd ../src/bt
mv settings.py settings_debug.py

if [[ $1 = 'local' ]]; then
    mv settings_static_local.py settings.py
else
    mv settings_static_nginx.py settings.py
fi

cd ${HOME}/${PROJ_DIR}/script

chmod u+x *.sh

source ./start.sh