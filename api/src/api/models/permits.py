from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

# --- Common Fields (Can be reused or extended in specific models) ---

class ContactInformation(BaseModel):
    full_name: str = Field(..., description="Full name of the applicant or contact person")
    phone_number: str = Field(..., description="Phone number for contact")
    email_address: str = Field(..., description="Email address for communication")
    address: str = Field(..., description="Primary address")
    identification_number: Optional[str] = Field(None, description="National ID or Business Registration Number (if applicable)")

class LocationInformation(BaseModel):
    full_address: str = Field(..., description="Full address of the location")
    property_identification_number: Optional[str] = Field(None, description="Parcel ID or Cadastral Number (if applicable)")
    legal_description: Optional[str] = Field(None, description="Legal description of the property (if required)")
    zoning_information: Optional[str] = Field(None, description="Zoning information (if applicable)")
    dimensions_area: Optional[str] = Field(None, description="Dimensions or area of the property/work area (if applicable)")

class SupportingDocument(BaseModel):
    name: str = Field(..., description="Name of the document")
    description: Optional[str] = Field(None, description="Brief description of the document")

# --- Models for Specific Permit Types ---

class BuildingPermitApplication(BaseModel):
    applicant_info: ContactInformation
    property_info: LocationInformation
    construction_description: str = Field(..., description="Detailed description of the proposed construction")
    start_date: Optional[datetime] = Field(None, description="Expected start date of construction")
    end_date: Optional[datetime] = Field(None, description="Expected end date of construction")
    building_plans_reference: Optional[str] = Field(None, description="Reference to uploaded building plans")
    materials_used: Optional[str] = Field(None, description="List of primary materials to be used")
    structural_engineer_details: Optional[ContactInformation] = Field(None, description="Details of the structural engineer (if applicable)")
    supporting_documents: Optional[List[SupportingDocument]] = Field(None, description="List of uploaded supporting documents")
    declaration: str = Field(..., description="Declaration statement")
    signature: str = Field(..., description="Applicant's signature (can be a digital representation)")
    application_date: datetime = Field(default_factory=datetime.utcnow, description="Date of application")

class EventPermitApplication(BaseModel):
    applicant_info: ContactInformation
    event_name: str = Field(..., description="Name of the event")
    location_info: LocationInformation
    start_datetime: datetime = Field(..., description="Start date and time of the event")
    end_datetime: datetime = Field(..., description="End date and time of the event")
    number_of_attendees: Optional[int] = Field(None, description="Estimated number of attendees")
    purpose_of_event: str = Field(..., description="Purpose and description of the event")
    event_schedule: Optional[str] = Field(None, description="Detailed schedule of activities")
    safety_plan_reference: Optional[str] = Field(None, description="Reference to uploaded safety plan")
    noise_level_management: Optional[str] = Field(None, description="Details on managing noise levels")
    waste_management_plan: Optional[str] = Field(None, description="Plan for managing waste")
    supporting_documents: Optional[List[SupportingDocument]] = Field(None, description="List of uploaded supporting documents")
    declaration: str = Field(..., description="Declaration statement")
    signature: str = Field(..., description="Applicant's signature (can be a digital representation)")
    application_date: datetime = Field(default_factory=datetime.utcnow, description="Date of application")

class BusinessLicenseApplication(BaseModel):
    applicant_info: ContactInformation
    business_name: str = Field(..., description="Name of the business")
    business_type: str = Field(..., description="Type of business (e.g., retail, service)")
    business_address: LocationInformation
    start_date: Optional[datetime] = Field(None, description="Date the business commenced or will commence")
    number_of_employees: Optional[int] = Field(None, description="Number of employees")
    nature_of_business: str = Field(..., description="Detailed description of the business activities")
    regulatory_compliance_details: Optional[str] = Field(None, description="Details of compliance with relevant regulations")
    supporting_documents: Optional[List[SupportingDocument]] = Field(None, description="List of uploaded supporting documents")
    declaration: str = Field(..., description="Declaration statement")
    signature: str = Field(..., description="Applicant's signature (can be a digital representation)")
    application_date: datetime = Field(default_factory=datetime.utcnow, description="Date of application")

# --- Generic Application Form (Can be used if the specific type isn't known yet) ---

class GenericPermitApplication(BaseModel):
    applicant_info: ContactInformation
    location_info: Optional[LocationInformation] = None
    project_activity_details: Dict[str, Optional[str]] = Field(..., description="Dictionary of fields specific to the permit type")
    supporting_documents: Optional[List[SupportingDocument]] = Field(None, description="List of uploaded supporting documents")
    declaration: str = Field(..., description="Declaration statement")
    signature: str = Field(..., description="Applicant's signature (can be a digital representation)")
    application_date: datetime = Field(default_factory=datetime.utcnow, description="Date of application")

# --- Model for Defining the Application Form Fields (as returned by /permits endpoint) ---

class ApplicationFormField(BaseModel):
    name: str = Field(..., description="Name of the form field")
    type: str = Field(..., description="Data type of the field (e.g., string, email, date, number)")
    required: bool = Field(False, description="Indicates if the field is mandatory")
    label: Optional[str] = Field(None, description="Human-readable label for the field")
    options: Optional[List[str]] = Field(None, description="Available options for select/dropdown fields")
    description: Optional[str] = Field(None, description="Help text or description for the field")

class PermitType(BaseModel):
    id: int
    name: str
    description: str
    application_form_fields: List[ApplicationFormField]

# --- Model for Submitting the Application Data (as expected by the /permits/{permit_id}/apply endpoint) ---

class SubmitApplicationRequest(BaseModel):
    user_id: str = Field(..., description="ID of the user submitting the application")
    form_data: Dict[str, Optional[str]] = Field(..., description="Dictionary containing the submitted form data")

class SubmitApplicationResponse(BaseModel):
    application_id: str
    message: str
    status: str

# --- Model for Displaying a User's Permit Applications ---

class PermitApplicationStatus(BaseModel):
    application_id: str
    permit_name: str
    submission_date: datetime
    status: str

# --- Model for Detailed Permit Application Information ---

class PermitApplicationDetails(PermitApplicationStatus):
    form_data: Dict[str, Optional[str]]

# --- Example of how you might use these models in your FastAPI routes ---
# (This is just a snippet and assumes you have a way to determine the permit type)

# @router.post("/{permit_id}/apply")
# async def apply_for_permit(permit_id: int, application_data: Dict):
#     # ... logic to determine the permit type based on permit_id
#     if permit_type == "building":
#         validated_data = BuildingPermitApplication(**application_data)
#         # ... process validated_data
#     elif permit_type == "event":
#         validated_data = EventPermitApplication(**application_data)
#         # ... process validated_data
#     # ...