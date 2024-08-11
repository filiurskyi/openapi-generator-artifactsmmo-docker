# openapi_client.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_accounts_create_post**](AccountsApi.md#create_account_accounts_create_post) | **POST** /accounts/create | Create Account


# **create_account_accounts_create_post**
> ResponseSchema create_account_accounts_create_post(add_account_schema)

Create Account

Create an account.

### Example


```python
import openapi_client
from openapi_client.models.add_account_schema import AddAccountSchema
from openapi_client.models.response_schema import ResponseSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountsApi(api_client)
    add_account_schema = openapi_client.AddAccountSchema() # AddAccountSchema | 

    try:
        # Create Account
        api_response = await api_instance.create_account_accounts_create_post(add_account_schema)
        print("The response of AccountsApi->create_account_accounts_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_accounts_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_account_schema** | [**AddAccountSchema**](AddAccountSchema.md)|  | 

### Return type

[**ResponseSchema**](ResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account created successfully. |  -  |
**456** | Username already used. |  -  |
**457** | Email already used. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

