#!/bin/bash

# Copyright (c) 2020-2029 GUARD Project <guard-project.eu>
# author: Alex Carrega <alessandro.carrega@cnit.it>

pipenv lock -r --dev-only > requirements-dev.txt
