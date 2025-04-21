@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/permits")
def get_avaolable_permits():

    json_response = [
      {
          "id": 1,
          "name": "Building Permit",
          "description": "Apply for permission to construct a new building.",
          "application_form_fields": [
              {"name": "full_name", "type": "string", "required": True},
              {"name": "email", "type": "email", "required": True},
              {"name": "property_address", "type": "string", "required": True},
              {"name": "construction_description", "type": "string", "required": True}
          ]
      },
      {
          "id": 2,
          "name": "Event Permit",
          "description": "Request authorization for a public event.",
          "application_form_fields": [
              {"name": "event_name", "type": "string", "required": True},
              {"name": "location", "type": "string", "required": True},
              {"name": "start_date", "type": "date", "required": True},
              {"name": "end_date", "type": "date", "required": True}
          ]
      }
    ]

    # Add more permits as needed
    return json_response


@app.post("/permits/{permit_id}/apply")
def submit_permit_application(permit_id: int, application_data: dict):
    """Submit new permit application."""
    # Here you would typically process the application data, save it to a database, etc.
    # For this example, we'll just return the received data.
    # 201 Created response or 500 Internal Server Error can be used based on the application processing result. 
    return {
    "application_id": "BP-2025-04-20-5678",
    "message": "Your application has been submitted successfully.",
    "status": "Pending",
    "permit_id": permit_id,
    }

@app.get("/permits/{permit_id}/status")
def get_permit_status(permit_id: int):
    """Get the status of a permit application."""
    # Here you would typically query the database for the application status.
    # For this example, we'll return a mock status.
    # 200 OK response or 404 Not Found can be used based on the application status or 400 Bad Request if the permit_id is invalid or 500 Internal Server Error if there is an issue with the server.
    return {
        "application_id": "BP-2025-04-20-5678",
        "status": "Pending",
        "permit_id": permit_id,
        "details": {
            "reviewer_comments": None,
            "estimated_processing_time": "2 weeks"
        }
    }


@app.get("/users/me/permits")
def get_user_permits():
    """Get all permits submitted by the user."""
    # Here you would typically query the database for the user's applications.
    # For this example, we'll return a mock list of applications.
    # 200 OK response or 401 Unauthorized can be used based on the authentication status or 500 Internal Server Error if there is an issue with the server.
    return [
        {
            "application_id": "BP-2025-04-20-5678",
            "status": "Pending",
            "permit_id": 1,
            "details": {
                "property_address": "123 Main St",
                "construction_description": "New residential building"
            }
        },
        {
            "application_id": "EP-2025-04-20-1234",
            "status": "Approved",
            "permit_id": 2,
            "details": {
                "event_name": "Community Festival",
                "location": "Central Park"
            }
        }
    ]



@app.get("/permits/applications/{application_id}")
def get_permit_application_details(application_id: str):
    """Get details of a specific permit application."""
    # Here you would typically query the database for the application details.
    # For this example, we'll return a mock application detail.
    # 200 OK response or 401 Unauthorized can be used based on the authentication status or 404 Not Found if the application_id is invalid or 500 Internal Server Error if there is an issue with the server.
    return {
        "application_id": application_id,
        "status": "Pending",
        "permit_id": 1,
        "details": {
            "property_address": "123 Main St",
            "construction_description": "New residential building",
            "reviewer_comments": None,
            "estimated_processing_time": "2 weeks"
        }
    }