FROM papagalu/kube-python-client:latest

RUN mkdir /portal

ADD portal_api /portal/portal_api
ADD server /portal/server
ADD pool/ /portal/pool
ADD main.py /portal/main.py
ADD __init__.py /portal/__init__.py

ADD deploy.yaml /deploy.yaml

ENTRYPOINT ["python3", "portal/main.py"]
