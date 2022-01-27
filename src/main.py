# Copyright (c) 2020-2029 GUARD Project <guard-project.eu>
# author: Alex Carrega <alessandro.carrega@cnit.it>

from fastapi import FastAPI

from src.about import version
from src.libs.console import header
from src.libs.settings import settings
from src.routers.commands import router as commands_router
from src.routers.configurations import router as configurations_router
from src.routers.parameters import router as parameters_router

header()

app = FastAPI(
    debug=settings.get("debug", False),
    title=settings.title,
    version=version,
    description=settings.description,
)

app.include_router(commands_router)
app.include_router(configurations_router)
app.include_router(parameters_router)
