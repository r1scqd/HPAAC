"""Containers module."""
import os

from dependency_injector import containers, providers

from .db.base import Database


def get_inject_modules():
    modules = []
    for root, dirs, files in os.walk('src'):
        if '__pycache__' in root:
            continue
        file: str
        for file in files:
            if file.endswith('.py') and file not in ('__init__.py', '__main__.py'):
                modules.append(os.path.join(root, file.removesuffix('.py')).replace(os.sep, '.'))
    return modules


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yaml"])

    db = providers.Singleton(Database, db_url=config.db.url)
