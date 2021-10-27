from aws_lambda_typing.events import (
    APIGatewayRequestAuthorizerEvent,
    APIGatewayTokenAuthorizerEvent,
)


def test_api_gateway_token_authorizer_event() -> None:
    event: APIGatewayTokenAuthorizerEvent = {
        "type": "TOKEN",
        "authorizationToken": "allow",
        "methodArn": "arn:aws:execute-api:us-west-2:123456789012:ymy8tbxw7b/*/GET/",  # noqa: E501
    }


def test_api_gateway_request_authorizer_event() -> None:
    event: APIGatewayRequestAuthorizerEvent = {
        "type": "REQUEST",
        "methodArn": "arn:aws:execute-api:us-east-1:123456789012:abcdef123/test/GET/request",  # noqa: E501
        "resource": "/request",
        "path": "/request",
        "httpMethod": "GET",
        "headers": {
            "X-AMZ-Date": "20170718T062915Z",
            "Accept": "*/*",
            "HeaderAuth1": "headerValue1",
            "CloudFront-Viewer-Country": "US",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Tablet-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "User-Agent": "...",
        },
        "queryStringParameters": {"QueryString1": "queryValue1"},
        "pathParameters": {},
        "stageVariables": {"StageVar1": "stageValue1"},
        "requestContext": {
            "path": "/request",
            "accountId": "123456789012",
            "resourceId": "05c7jb",
            "stage": "test",
            "requestId": "...",
            "identity": {
                "apiKey": "...",
                "sourceIp": "...",
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",  # noqa: E501
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT",
                    },
                },
            },
            "resourcePath": "/request",
            "httpMethod": "GET",
            "apiId": "abcdef123",
        },
    }
