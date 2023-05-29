#!/bin/bash

PARAMETER_IDENTIFIER=$PARAMETER_IDENTIFIER

APP_REFERENCE=$APP_REFERENCE

ENVIRONMENT_REFERENCE=$ENVIRONMENT_REFERENCE

AWS_PARAMETERS_LIST=$(aws ssm describe-parameters --query "Parameters[?Name.contains(@, '$PARAMETER_IDENTIFIER')] [].[Name]" --output text)

for parameter in $AWS_PARAMETERS_LIST
do
    SHORT_AWS_PARAMETER_NAME=$(echo $parameter | sed 's/\'$ENVIRONMENT_REFERENCE'\'$APP_REFERENCE'\///g' | tr '[:lower:]' '[:upper:]')
    PARAMETER_VALUE=$(aws ssm get-parameter --name $parameter --query Parameter.Value --output text)
    echo "$SHORT_AWS_PARAMETER_NAME=$PARAMETER_VALUE" >> $GITHUB_ENV
done

# This script does not contain the optimization to avoid the throttling error in calling the API.
