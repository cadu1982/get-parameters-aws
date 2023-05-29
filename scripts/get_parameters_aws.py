#!/usr/bin/env python3

import boto3
import os
from botocore.config import Config


def get_parameters_aws(ssm_client, parameter_identifier):

    paginator = ssm_client.get_paginator('get_parameters_by_path')

    page_iterator = paginator.paginate(Path = parameter_identifier)

    parameters = []

    for page in page_iterator:
        for parameter in page['Parameters']:    
            name = parameter['Name']
            new_name = name[(len(parameter_identifier)):]
            value = parameter['Value']
            parameters.append(new_name + '=' + value)

    return parameters


def set_parameters_environment_vars(all_parameters):

    env_file = os.getenv('GITHUB_ENV')

    for parameters in all_parameters:
        with open(env_file, "a") as myfile:
            myfile.write(parameters + "\n")

    return myfile


def main():

    # Variables Declaration
    parameter_identifier = os.environ['PARAMETER_IDENTIFIER']

    # Import AWS Service
    ssm_client = boto3.client('ssm', config=Config(connect_timeout=5, read_timeout=60, retries={'max_attempts': 20}))
    
    # Get Parameters From AWS
    all_parameters = get_parameters_aws(ssm_client, parameter_identifier)

    # Set Parameters As Environment Variables
    if all_parameters != []:
        set_parameters_environment_vars(all_parameters)


if __name__ == '__main__':
    main()