from fastapi import APIRouter, Depends
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime

# Define Pydantic models for request and response bodies (optional but recommended)



router = APIRouter(prefix="/permits", tags=["Permits"])

# In-memory data for demonstration purposes (replace with database interactions)
available_permits = [
        {
            "id": 1,
            "name": "Building Permit",
            "description": "Apply for permission to construct a new building.",
            "application_form_fields": [
                {"name": "full_name", "type": "string", "required": True},
                {"name": "email", "type": "email", "required": True},
                {"name": "property_address", "type": "string", "required": True},
                {"name": "construction_description", "type": "string", "required": True},
            ],
        },
        {
            "id": 2,
            "name": "Event Permit",
            "description": "Request authorization for a public event.",
            "application_form_fields": [
                {"name": "event_name", "type": "string", "required": True},
                {"name": "location", "type": "string", "required": True},
                {"name": "start_date", "type": "date", "required": True},
                {"name": "end_date", "type": "date", "required": True},
                {"name": "organizer_name", "type": "string", "required": True},
            ],
        },
]

permit_applications = []

# --- Permits Service Endpoints ---

@router.get("/")
async def get_available_permits():
    """
    Returns a list of all available permit types with their descriptions and required form fields.
    """
    return available_permits

@router.post("/{permit_id}/apply")
async def apply_for_permit(permit_id: int, application_data: Dict[str, str]):
    """
    Submits a new application for a specific permit.
    """
    permit = next((p for p in available_permits if p.id == permit_id), None)
    if not permit:
        return {"application_id": None, "message": "Permit not found.", "status": "Failed"}

    application_id = f"APP-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{permit_id}"
    new_application = {
        "application_id": application_id,
        "permit_name": permit.name,
        "submission_date": datetime.utcnow(),
        "status": "Pending",
        "form_data": application_data.form_data,
    }
    permit_applications.append(new_application)
    return {"application_id": application_id, "message": "Your application has been submitted successfully.", "status": "Pending"}

# @router.get("/applications/me", response_model=List[PermitApplication])
# async def get_user_permit_applications(user_id: str = "user-123"): # Replace with actual authentication
#     """
#     Returns a list of the current user's permit applications.
#     """
#     user_applications = [app for app in permit_applications if app["form_data"].get("user_id") == user_id or application_data.user_id == user_id] # Simple filtering for demonstration
#     # In a real application, you would fetch based on the authenticated user.
#     return [PermitApplication(**app) for app in user_applications]

@router.get("/applications/{application_id}")
async def get_specific_permit_application(application_id: str):
    """
    Returns the details of a specific permit application.
    """
    application = next((app for app in permit_applications if app["application_id"] == application_id), None)
    if application:
        return {**application, "status": "Success"}
    return None