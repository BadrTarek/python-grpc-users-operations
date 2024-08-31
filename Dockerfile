FROM python:3.8-alpine

# Install the required packages
RUN apk update && \
    apk add --no-cache \
    build-base  \
    libffi-dev \
    make \
    python3 \
    python3-dev &&\
    pip install --upgrade pip

# Copy the project files into the image
COPY src/ /src/
COPY requirements.txt .
COPY tests/ /tests/
COPY requirements-test.txt .
COPY Makefile .

# Install the dependencies & Generate the protobufs files & Run the tests & Run the safety check & Remove temporary files
RUN make install && \
    make generate-protos && \
    make unit-test && \
    pip install safety && \
    pip freeze | safety check --stdin --full-report -i 70612  && \
    rm -rf /tests  && \
    pip uninstall -y safety && \
    pip uninstall -r requirements-test.txt -y && \
    rm requirements-test.txt && \
    rm requirements.txt

# Set the environment variables
ENV GRPC_SERVER_PORT=50051

# Expose the gRPC server port
EXPOSE $GRPC_SERVER_PORT

# Run the gRPC server when the container starts
ENTRYPOINT ["make", "start"]