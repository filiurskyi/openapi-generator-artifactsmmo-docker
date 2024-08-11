# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status_get**](DefaultApi.md#get_status_get) | **GET** / | Get Status


# **get_status_get**
> StatusResponseSchema get_status_get()

Get Status

Return the status of the game server.

### Example


```python
import openapi_client
from openapi_client.models.status_response_schema import StatusResponseSchema
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Status
        api_response = await api_instance.get_status_get()
        print("The response of DefaultApi->get_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusResponseSchema**](StatusResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

