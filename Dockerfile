FROM python:alpine3.9

EXPOSE 5000

COPY . /app
WORKDIR /app

RUN  apk add --no-cache libgfortran build-base libstdc++ \
                        libpng libpng-dev \
                        freetype freetype-dev && \
    # Install Python dependencies
    pip3 install -v --no-cache-dir flask==1.0.2 matplotlib==3.0.3 && \
    # Cleanup
    apk del --purge build-base libgfortran libpng-dev freetype-dev && \
    rm -vrf /var/cache/apk/*

CMD python ./index.py
