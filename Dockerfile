FROM python:3.8.0-slim AS app

# Install the required packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential libjpeg-dev git gcc python3-dev musl-dev libffi-dev && \
    apt-get clean && \
    apt-get install -y make && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip


# Copy the project files into the image
COPY src/ /src/
COPY requirements.txt .
COPY tests/ /tests/
COPY requirements-test.txt .
COPY Makefile .

# Install the project dependencies
RUN make install

# Generate the protobufs files
RUN make generate-protos

# Run the tests and linters 
RUN make unit-test

# Run the safety check
RUN pip install safety
RUN pip freeze | safety check --stdin --full-report -i 70612

# Remove the tests directory
RUN rm -rf /tests
RUN pip uninstall -y safety
RUN pip uninstall -r requirements-test.txt -y
RUN rm requirements-test.txt

# Expose the gRPC server port
EXPOSE 50051

# Run the gRPC server when the container starts
ENTRYPOINT ["make", "start"]