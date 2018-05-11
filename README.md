# Portal

Portal is a framework that enables game developers to focus on the game and not
on the infrastructure.

It leverages the features of kubernetes and speed of containers to dynamically
spawn containers that would run the game server.

## Demo

Please install minikube
kubernetes version 1.10


get admin rights for the default namespace and service account
```bash
kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin  --serviceaccount=default:default
```

build the Docker image
```bash
$ eval $(minikube docker-env)
$ cd portal
$ docker build -t <insert cool name here> .
$ # edit deploy.yaml with the same cool name
$ kubectl apply -f deploy.yaml
$ eval $(minikube docker-env -u)
```
