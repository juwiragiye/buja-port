from fastapi import APIRouter
import os
import importlib.util

router = APIRouter()

def include_routes_from_folder(router: APIRouter, folder_path: str):
    """
    Includes routes from all Python files within the specified folder.
    Assumes each file in the folder defines an APIRouter instance named 'router'.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            file_path = os.path.join(folder_path, filename)

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Check if the module has an APIRouter instance named 'router'
            if hasattr(module, "router") and isinstance(getattr(module, "router"), APIRouter):
                router.include_router(module.router)
            else:
                print(f"Warning: File '{filename}' in '{folder_path}' does not define an APIRouter named 'router'.")

# Assuming your route files are in a folder named 'routes' in the same directory as this file
routes_folder = "routes"
include_routes_from_folder(router, routes_folder)

