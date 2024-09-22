# First stage: build the Go application
FROM golang:1.20 AS builder

# Set the working directory
WORKDIR /app

# Copy the Go module files and install dependencies (if any)
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code
COPY . .

# Build the application
RUN go build -o hello-go .

# Second stage: create a lean image
FROM alpine:latest

# Copy the compiled binary from the builder stage
COPY --from=builder /app/hello-go /usr/local/bin/hello-go

# Set the entry point to the application
ENTRYPOINT ["/usr/local/bin/hello-go"]
