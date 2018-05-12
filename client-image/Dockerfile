FROM alpine:3.6

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ENV KUBE_CLIENT_VERSION="6.0.0"
	
RUN apk add --update --no-cache \
		dumb-init \
		bash \
		sudo \
		python \
                alpine-sdk \
	&& apk add --no-cache \
		python-dev \
		py-pip \
	&& pip install --no-cache-dir -U \
		passlib \
                grpcio-tools \
		kubernetes==${KUBE_CLIENT_VERSION} \
	&& rm -fr \
		/var/cache/apk/* \
		/root/.cache \
		/tmp/*

CMD ["/bin/bash"]
