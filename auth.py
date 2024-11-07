from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer


azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id='36cca2d3-b896-4199-9288-9663cd79221a',
    tenant_id='69cc1df0-9926-43ec-941d-2f534db013bc',
    scopes={'https://testmsalintegration.onmicrosoft.com/auth-backend/access_as_user':'access_as_user'},
    allow_guest_users=True
)