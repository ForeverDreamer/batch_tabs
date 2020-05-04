#!/usr/bin/env bash

set -x

set -eo pipefail

ROOT_DIR=..

#if [[ ! -d ${ROOT_DIR}/assets ]]; then
#    mkdir ${ROOT_DIR}/assets
#fi

if [[ ! -d ${ROOT_DIR}/log ]]; then
    mkdir ${ROOT_DIR}/log && touch ${ROOT_DIR}/log/django.log ${ROOT_DIR}/log/mm.log && chmod -R 777 ${ROOT_DIR}/log
fi