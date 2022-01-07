from dapr.ext.grpc import App, BindingRequest
from dapr.clients import DaprClient
import json

app = App()

@app.binding('testpythonapps')
def binding(request: BindingRequest):
    print(request.text(), flush=True)
    payload = {"videoID":"615eada740df58bbc58cf4859"}
    with DaprClient() as d:
        response = d.invoke_method(
            'teambyocr',
            'teambyocr',
            data=json.dumps(payload),
        )
    print(json.loads(response.text()))

if __name__ == "__main__":
    app.run(50059) # run on the server
