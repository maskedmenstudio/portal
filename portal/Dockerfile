FROM papagalu/kube-python-client

RUN mkdir /portal

ADD portal_api /portal/portal_api
ADD server /portal/server
ADD main.py /portal/main.py
ADD __init__.py /portal/__init__.py

ENTRYPOINT ["python", "portal/main.py"]
