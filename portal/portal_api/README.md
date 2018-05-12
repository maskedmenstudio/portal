we use grpc

Lets install the grpc compiler
```bash
$ pip install grpcio-tools
```

How to generate gRPC classes for Python
```bash
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. grpc/api.proto
```
