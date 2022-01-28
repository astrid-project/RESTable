# Copyright (c) 2020-2029 GUARD Project (https://www.guard-project.eu)
# author: Alex Carrega <alessandro.carrega@cnit.it>

from __future__ import annotations

import json
from enum import Enum
from subprocess import CompletedProcess
from typing import Any, Callable, Dict, List

import yaml
from fastapi import APIRouter

from src.libs.base import Base, Format
from src.libs.settings import settings

router = APIRouter()


class Parameters(Base):
    class Id(str, Enum):
        pass

    label = "parameter"
    data = settings.get("parameters", [])

    class SettingsModel(Base.Model):
        source: str
        format: Format
        xpath: List[str]

    class OutputModel(SettingsModel):
        value: Any


Parameters.makeIDs()


@router.get("/parameters")
def get() -> Dict[Parameters.Id, Parameters.OutputModel]:
    return {parameter: get_record(parameter) for parameter in Parameters.Id}


@router.get("/parameters/{id}")
def get_record(id: Parameters.Id) -> Parameters.OutputModel:
    parameter = Parameters.get(id)
    read(parameter, format="yaml", loader=yaml.load)
    read(parameter, format="json", loader=json.load)
    return parameter


@router.post("/parameters")
def set(data: Dict[Parameters.Id, Any]) -> Dict[Parameters.Id, Parameters.ActionModel]:
    return {id: set_record(id, value) for id, value in data.items()}


@router.post("/parameters/{id}")
def set_record(id: Parameters.Id, value: Dict[Any, Any]) -> Parameters.ActionModel:
    return set_record_inline(id, value)


@router.post("/parameters/{id}/{value}")
def set_record_inline(id: Parameters.Id, value: Any) -> Parameters.ActionModel:
    def __set(parameter: Parameters.SettingsModel, value: Any) -> CompletedProcess[str]:
        write(parameter, value, format="yaml", loader=yaml.load, dumper=yaml.dump)
        write(parameter, value, format="json", loader=json.load, dumper=json.dump)
        return CompletedProcess([], returncode=0, stdout="", stderr="")

    return Parameters.action(id, __set, value=value)


def read(data: Parameters.SettingsModel, format: str, loader: Callable) -> None:
    if data.format == format:
        with open(data.source, "r") as file:
            content = loader(file)
            value = content
            for x in data.xpath:
                value = value[x]
        data.update(value=value)


def write(
    data: Parameters.SettingsModel,
    value: any,
    format: str,
    loader: Callable,
    dumper: Callable,
) -> None:
    if data.format == format:
        read(data, format=format, loader=loader)
        with open(data.source, "r") as file:
            content = loader(file)
            dest = content
            for x in data.xpath[:-1]:
                dest = dest[x]
            dest[data.xpath[-1]] = value
        with open(data.source, "w") as file:
            dumper(content, file)
