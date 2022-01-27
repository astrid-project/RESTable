#!/bin/sh

# Copyright (c) 2020-2029 GUARD Project <guard-project.eu>
# author: Alex Carrega <alessandro.carrega@cnit.it>

vprof -c cmh src/main.py --output-file dev/profile.json
