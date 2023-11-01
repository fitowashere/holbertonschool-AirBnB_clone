#!/usr/bin/env python3

import os
import shutil

def delete_pycache(startpath):
    for root, dirs, files in os.walk(startpath):
        if '__pycache__' in dirs:
            print(f"Deleting: {os.path.join(root, '__pycache__')}")
            shutil.rmtree(os.path.join(root, '__pycache__'))

if __name__ == "__main__":
    start_path = "."  # Start from the current directory, change as needed
    delete_pycache(start_path)
    print("Deletion of __pycache__ folders complete.")
