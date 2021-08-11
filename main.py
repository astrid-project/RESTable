# Copyright (c) 2020-2029 Alex Carrega <contact@alexcarrega.com>
# author: Alex Carrega <contact@alexcarrega.com>

import subprocess
from datetime import datetime
from enum import Enum

from aenum import extend_enum
from dynaconf import Dynaconf
from fastapi import FastAPI, HTTPException

from about import version

settings = Dynaconf(
    settings_files=["settings.yaml", ".secrets.yaml"]
)

app = FastAPI(debug=settings.get('debug', False), title=settings.name, version=version, description=settings.description)


class CommandId(str, Enum):
    pass


for cmd in settings.commands.keys():
    extend_enum(CommandId, cmd, cmd)


history = {}
for command in settings.commands:
    history[command] = []


@app.get('/')
def view_commands():
    return settings.commands


@app.get('/{command}')
def view_command(command: CommandId):
    if command not in settings.commands:
        raise HTTPException(
            status_code=404, detail=f'Command {command} not found')
    output = settings.commands.get(command)
    output['history'] = history[command]
    return output


@app.post('/{command}')
def execute_command(command: CommandId):
    print(command)
    if command not in settings.commands:
        raise HTTPException(
            status_code=404, detail=f'Command {command} not found')
    start = datetime.now()
    proc = run_script(command)
    end = datetime.now()
    output = {
        'error': proc.returncode == None or proc.returncode > 0,
        'stdout': process_data(proc.stdout),
        'stderr': process_data(proc.stderr),
        'returncode': proc.returncode,
        'start': start,
        'end': end
    }
    history[command].append(output)
    return output


def process_data(data: str):
    tmp = map(lambda item: item.strip(), data.split('\n'))
    return list(filter(lambda item: item, tmp))


def run_script(command: str):
    command_data = settings.commands.get(command)
    print(command_data.script)
    if not command_data.get('daemon', False):
        return subprocess.run(command_data.script, check=False, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    else:
        return subprocess.Popen(command_data.script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
