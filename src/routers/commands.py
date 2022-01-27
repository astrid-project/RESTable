# Copyright (c) 2020-2029 GUARD Project <guard-project.eu>
# author: Alex Carrega <alessandro.carrega@cnit.it>

from __future__ import annotations

from enum import Enum
from subprocess import PIPE, CompletedProcess, Popen, run
from typing import Dict, Optional

from fastapi import APIRouter

from src.libs.base import Base
from src.libs.settings import settings

router = APIRouter()


class Commands(Base):
    class Id(str, Enum):
        pass

    label = "command"
    data = settings.get("commands", [])

    class SettingsModel(Base.Model):
        script: str
        daemon: Optional[bool] = False

    class OutputModel(SettingsModel):
        pass


Commands.makeIDs()


@router.get("/commands", description="List all available command settings")
def get() -> Dict[Commands.Id, Commands.OutputModel]:
    return {command: get_record(command) for command in Commands.Id}


@router.get("/commands/{id}", description="Get the command settings")
def get_record(id: Commands.Id) -> Commands.OutputModel:
    return Commands.get(id)


@router.post("/commands", description="Execute a set of commands")
def set() -> Dict[Commands.Id, Commands.ActionModel]:
    return {command: set_record(command) for command in Commands.Id}


@router.post("/commands/{id}", description="Execute a command")
def set_record(id: Commands.Id) -> Commands.ActionModel:
    def __set_record(command: Commands.SettingsModel) -> CompletedProcess[str] | Popen:
        if not command.get("daemon", False):
            return run(
                command.script,
                check=False,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                universal_newlines=True,
            )
        else:
            return Popen(
                command.script,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                start_new_session=True,
            )

    return Commands.action(id, __set_record)
