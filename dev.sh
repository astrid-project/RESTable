#!/bin/sh

PORT=$(cat settings.yaml | shyaml get-value port)
uvicorn main:app --reload --port $PORT