from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Callable, Dict, List, Type, TypeVar

from aenum import extend_enum
from fastapi import HTTPException
from pydantic import BaseModel

T = TypeVar("T", bound="Base")


class Base:
    class ActionModel(BaseModel):
        error: bool
        stdout: List[str]
        stderr: List[str]
        returncode: int
        start: datetime
        end: datetime

    class Model(BaseModel):
        history: List[Base.ActionModel]

    @classmethod
    def makeIDs(cls: Type[T]) -> None:
        for id in cls.data:
            extend_enum(cls.Id, id, id)

    @classmethod
    def get(cls: Type[T], id: T.Id) -> T.SettingModel:
        if id not in cls.data:
            raise HTTPException(
                status_code=404, detail=f"{cls.label.title()} {id} not found"
            )
        return cls.data.get(id)

    @classmethod
    def add(cls: Type[T], id: str, data: Dict[T.ActionModel]) -> None:
        if "history" not in cls.data[id]:
            cls.data[id]["history"] = []
        cls.data[id]["history"].append(data)

    @staticmethod
    def process(data: str) -> List[str]:
        __process = map(lambda item: item.strip(), data.split("\n"))
        return list(filter(lambda item: item, __process))

    @classmethod
    def action(
        cls: Type[T], id: T.Id, callback: Callable, **callback_kwargs: Dict[any, any]
    ) -> T.ActionModel:
        start = datetime.now()
        res = callback(cls.get(id), **callback_kwargs)
        end = datetime.now()
        data = cls.ActionModel(
            error=res.returncode is None or res.returncode > 0,
            stdout=cls.process(res.stdout),
            stderr=cls.process(res.stderr),
            returncode=res.returncode,
            start=start,
            end=end,
        )
        cls.add(id, data)
        return data


class Format(str, Enum):
    yaml = "yaml"
    json = "json"
