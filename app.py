import windows

def lambda_handler(event, context):
    """
    AWS Lambda handler test function

    Parameters:
    event (dict): Event data passed by AWS Lambda.
    context (LambdaContext): Runtime information provided by AWS Lambda.

    Returns:
    dict: A response object with statusCode and body.
    """
    print("Received event:", json.dumps(event))

    # Example: Handle different HTTP methods if triggered via API Gateway
    method = event.get("httpMethod", "GET")
    if method == "GET":
        body = {"message": "Hello Lambda test!"}
    elif method == "POST":
        data = json.loads(event.get("body", "{}"))
        body = {"message": "Data received", "data": data}
    else:
        body = {"error": "Unsupported method"}

    return {
        "statusCode": 400,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
