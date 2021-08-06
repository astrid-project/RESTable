#!/bin/sh

PORT=$(cat settings.yaml | shyaml get-value port)
uvicorn main:app --host 0.0.0.0 --port $PORT
