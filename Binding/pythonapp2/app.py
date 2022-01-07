from dapr.ext.grpc import App, BindingRequest

app = App()

@app.binding('testpythonapps')
def binding(request: BindingRequest):
    print(request.text(), flush=True)

if __name__ == "__main__":
    app.run(3000) # run on the server
