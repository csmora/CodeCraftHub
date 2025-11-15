import json
import os

def create_structure_from_json(json_data, base_path="."):
    """
    Creates a directory and file structure based on a JSON dictionary.

    Args:
        json_data (dict): The JSON dictionary representing the structure.
        base_path (str): The starting path for creating the structure.
    """
    for name, content in json_data.items():
        full_path = os.path.join(base_path, name)

        
        if isinstance(content, dict):  # It's a directory
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
            create_structure_from_json(content, full_path)
        # else:
            # print(f"Warning: Unrecognized content type for '{name}'. Skipping.")
        else: #content is None:  # It's a file
            with open(full_path, 'w') as f:
                f.write("")  # Create an empty file
            print(f"Created file: {full_path}")

# Example usage:
json_string = """
{
  "projectRoot": {
    "src": {
      "config": {
        "index.js": "Centralized configuration management (env variables, DB URIs, secrets)",
        "db.js": "MongoDB connection setup and initialization"
      },
      "controllers": {
        "userController.js": "Handles incoming HTTP requests related to user operations"
      },
      "models": {
        "userModel.js": "Mongoose schema and model for User"
      },
      "routes": {
        "userRoutes.js": "Express routes for user endpoints"
      },
      "services": {
        "userService.js": "Business logic for user management, separate from controllers"
      },
      "middlewares": {
        "authMiddleware.js": "JWT authentication and authorization middleware",
        "errorMiddleware.js": "Centralized error handling middleware",
        "validationMiddleware.js": "Request validation logic using libraries like Joi or celebrate"
      },
      "utils": {
        "logger.js": "Logging utility",
        "responseHandler.js": "Standardized API response formatting"
      },
      "validators": {
        "userValidator.js": "Schemas and validation rules for user input"
      },
      "app.js": "Express app initialization and middleware setup",
      "server.js": "Server startup script"
    },
    "tests": {
      "unit": {
        "userService.test.js": "Unit tests for user service logic"
      },
      "integration": {
        "userRoutes.test.js": "Integration tests for user routes and controllers"
      }
    },
    ".env.example": "Example environment variables file",
    ".gitignore": "Ignore node_modules, logs, .env files",
    "package.json": "Dependencies and scripts",
    "README.md": "Project overview and setup instructions",
    "dockerfile": "Dockerfile for containerizing the service",
    "docker-compose.yml": "Optional for local development with MongoDB"
  }
}
"""

# Load the JSON data
data = json.loads(json_string)

# Create the directory structure
create_structure_from_json(data)