# Copyright (c) 2020-2029 GUARD Project (https://www.guard-project.eu)
# author: Alex Carrega <alessandro.carrega@cnit.it>

from dynaconf import Dynaconf

settings = Dynaconf(settings_files=["settings.yaml", ".secrets.yaml"])
