#!/bin/bash

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if required arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <access-key-id> <secret-access-key> [OPTIONAL]<session-token>"
    exit 1
fi

export AWS_ACCESS_KEY_ID="$1"
export AWS_SECRET_ACCESS_KEY="$2"

# the session token is required when using temporary keys
if [ $# -eq 3 ]; then
    export AWS_SESSION_TOKEN="$3"
fi

# Get the identity associated with the keys (and the session token if using temporary keys)
aws sts get-caller-identity