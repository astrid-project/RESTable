#!/bin/sh

PORT=$(cat settings.yaml | shyaml get-value port)
uvicorn main:app --reload --host 0.0.0.0 --port $PORT
