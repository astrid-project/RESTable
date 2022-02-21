# Copyright (c) 2020-2029 ASTRID Project (https://www.astrid-project.eu)
# author: Alex Carrega <alessandro.carrega@cnit.it>

from rich import pretty, traceback  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.panel import Panel  # noqa: E402

from src.about import version
from src.libs.settings import settings

pretty.install()
traceback.install(show_locals=settings.get("debug", False))


def header() -> None:
    ident: str = f"{settings.project} - {settings.title} v:{version}"
    console = Console()
    console.print(Panel.fit(ident))
