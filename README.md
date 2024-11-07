# FastAPI MSAL Backend

This is a FastAPI project integrated with Azure Active Directory (Azure AD) for user authentication, utilizing the Microsoft Authentication Library (MSAL). This project aims to provide a secure backend that is used in conjunction with a frontend application built using React.js. The authentication flow involves the use of OAuth 2.0 access tokens for secure interaction between the frontend and backend services.

## Table of Contents
- [Introduction](#introduction)
- [Technology Stack](#technology-stack)
- [Azure AD App Registration](#azure-ad-app-registration)
- [How Authentication Works](#how-authentication-works)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [License](#license)

## Introduction
This backend is part of a system that allows users within an organization to securely access resources using Microsoft Azure Active Directory. Users authenticate via the frontend React application, which acquires tokens from Azure AD and communicates with this backend.

The core technology used for authentication here is **MSAL (Microsoft Authentication Library)** and **Azure Active Directory** to implement secure, token-based authentication and authorization.

## Technology Stack
- **Python**
- **FastAPI** - Framework for building APIs with Python.
- **Uvicorn** - ASGI server to serve FastAPI.
- **FastAPI-Azure-Auth** - Library used for Azure AD authentication.
- **Microsoft Azure AD** - Authentication and Authorization.

## Azure AD App Registration
To use Azure AD for authentication, you need to register two separate applications in Azure AD:

1. **Frontend Application**: This application is used by the React frontend for user login.
2. **Backend Application**: This application is used by the FastAPI backend to verify the user's access tokens.

### Steps for Azure AD Registration
1. **Frontend App Registration**:
    - Register an app called `React Frontend App`.
    - Set up **Redirect URI** to `http://localhost:5173`.
    - Define permissions to allow communication with the backend API.

2. **Backend App Registration**:
    - Register another app called `FastAPI Backend App`.
    - Expose an API and define scopes, e.g., `api://<client-id>/access_as_user`.
    - Set permissions for the frontend app to access the backend API.

## How Authentication Works
The authentication flow follows the standard **OAuth 2.0 Authorization Code Flow** with MSAL for the frontend and backend communication.

### Step-by-Step Authentication Flow
1. **Frontend Login**:
   - The **React frontend** application utilizes **MSAL.js** to prompt the user to log in via Azure AD.
   - Upon successful login, the frontend acquires an **access token** from Azure AD.

2. **Access Token**:
   - This **access token** is used to authenticate API requests to the FastAPI backend.
   - The token is passed in the `Authorization` header of each request in the format:
     ```http
     Authorization: Bearer <access_token>
     ```

3. **Backend Token Validation**:
   - The **FastAPI backend** validates the access token using the **FastAPI-Azure-Auth** library.
   - The token is decoded to ensure that it was issued by Azure AD, and to verify that the token's scope matches the permissions required by the backend API.
   - Once the token is verified, the backend processes the request and provides the response.

### Token Handling
- **Access Token**: The token contains information about the user, such as the user ID and scope permissions.
- **Token Logging**: The backend is set up to log the received tokens for debugging purposes. This can be useful for verifying the token structure and checking if the correct permissions are being provided.

### FastAPI-Azure-Auth Integration
- In the backend, `SingleTenantAzureAuthorizationCodeBearer` from **FastAPI-Azure-Auth** is used to simplify Azure AD integration.
- The **`azure_scheme`** is defined in `auth.py` and imported in other modules (e.g., `users.py`, `main.py`) to enforce authentication where required.

## Getting Started
To get this backend running locally, follow these steps:

### Prerequisites
- **Python 3.7+**
- **Git**
- **Azure AD App Registrations**
- **Frontend Application (React)** for user login

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/fastapi-msal-backend.git
   cd fastapi-msal-backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```
   The application will start running on **http://127.0.0.1:8000**.

### .env File Setup
Create a `.env` file to store sensitive configuration values such as **Client ID** and **Tenant ID**. This will make your development environment cleaner and safer.

## Endpoints
The backend has several endpoints, including a protected `/api/users` endpoint.

- **GET /api/users**: Returns a list of users from the `users.json` file.
  - This endpoint is **protected** and requires a valid **access token**.
  - To access this endpoint, the client must include a valid `Authorization` header.

---
