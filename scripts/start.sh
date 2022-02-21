#!/bin/bash

# Copyright (c) 2020-2029 ASTRID Project (https://www.astrid-project.eu)
# author: Alex Carrega <alessandro.carrega@cnit.it>

PORT=$(cat settings.yaml | shyaml get-value port)
uvicorn src.main:app --host 0.0.0.0 --port $PORT
