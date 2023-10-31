#!/usr/bin/python3
""" File storage engine """
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()