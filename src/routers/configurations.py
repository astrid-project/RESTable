# Copyright (c) 2020-2029 GUARD Project <guard-project.eu>
# author: Alex Carrega <alessandro.carrega@cnit.it>

from __future__ import annotations

import json
from enum import Enum
from subprocess import CompletedProcess
from typing import Any, Callable, Dict

import yaml
from fastapi import APIRouter
from pydantic import BaseModel

from src.libs.base import Base, Format
from src.libs.settings import settings

router = APIRouter()


class Configurations(Base):
    class Id(str, Enum):
        pass

    label = "configuration"
    data = settings.configurations

    class SettingsModel(BaseModel):
        path: str
        format: Format

    class OutputModel(SettingsModel):
        content: Any


Configurations.makeIDs()


@router.get("/configurations")
def get() -> Dict[Configurations.Id, Configurations.OutputModel]:
    return {
        configuration: get_record(configuration) for configuration in Configurations.Id
    }


@router.get("/configurations/{id}")
def get_record(id: Configurations.Id) -> Configurations.OutputModel:
    data = Configurations.get(id)
    read(data, format="yaml", loader=yaml.load)
    read(data, format="json", loader=json.load)
    return data


@router.post("/configurations")
def set(
    data: Dict[Configurations.Id, Any],
) -> Dict[Configurations.Id, Configurations.ActionModel]:
    return {id: set_record(id, content) for id, content in data.items()}


@router.post("/configurations/{id}")
def set_record(
    id: Configurations.Id, content: Dict[Any, Any]
) -> Configurations.ActionModel:
    def __set(configuration: Configurations.Id, content: Any) -> CompletedProcess[str]:
        write(configuration, content, format="yaml", dumper=yaml.dump)
        write(configuration, content, format="json", dumper=json.dump)
        return CompletedProcess([], returncode=0, stdout="", stderr="")

    return Configurations.action(id, __set, content=content)


def read(data: Configurations.SettingsModel, format: str, loader: Callable) -> None:
    if data.format == format:
        with open(data.path, "r") as file:
            data.update(content=loader(file))


def write(
    data: Configurations.SettingsModel, content: Any, format: str, dumper: Callable
) -> None:
    if data.format == format:
        with open(data.path, "w") as file:
            dumper(content, file)
