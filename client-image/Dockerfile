FROM alpine:3.6

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ENV KUBE_CLIENT_VERSION="6.0.0"
	
RUN apk add --update --no-cache \
		dumb-init \
		bash \
		sudo \
                python3 \
                alpine-sdk \
		python3-dev \
		py-pip \
	&& pip3.6 install --no-cache-dir -U \
		passlib \
                grpcio-tools \
		kubernetes==${KUBE_CLIENT_VERSION} \
	&& rm -fr \
		/var/cache/apk/* \
		/root/.cache \
		/tmp/*

CMD ["/bin/bash"]
