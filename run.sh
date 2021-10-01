#!/bin/sh

# Copyright (c) 2020-2029 Alex Carrega <contact@alexcarrega.com>
# author: Alex Carrega <contact@alexcarrega.com>

PORT=$(cat settings.yaml | shyaml get-value port)
uvicorn src.main:app --host 0.0.0.0 --port $PORT
