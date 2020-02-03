#!/usr/bin/env python
import subprocess
import boto3

# # 외부 shell에서 실행할 결과를 변수에 할당
# access_key = subprocess.run(
#     'aws configure get aws_access_key_id --profile wps-secrets-manager',
#     stdout=subprocess.PIPE,
#     shell=True
# ).stdout.decode('utf-8').strip()
#
# secret_key = subprocess.run(
#     'aws configure get aws_secret_access_key --profile wps-secrets-manager',
#     stdout=subprocess.PIPE,
#     shell=True
# ).stdout.decode('utf-8').strip()
#
# print('access_key >>> ', access_key)
# print('secret_key >>> ', secret_key)

# boto3 사용
session = boto3.session.Session(profile_name='wps-secrets-manager')
credentials = session.get_credentials()
access_key = credentials.access_key
secret_key = credentials.secret_key

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    ('-p', '8001:8000'),
    ('--name', 'instagram'),
    ('--env', f'AWS_SECRETS_MANAGER_ACCESS_KEY_ID={access_key}'),
    ('--env', f'AWS_SECRETS_MANAGER_SECRET_ACCESS_KEY={secret_key}'),
]

DOCKER_IMAGE_TAG = 'raccoonhj33/200128-instagram'

subprocess.run(f'docker build -t {DOCKER_IMAGE_TAG} -f Dockerfile .', shell=True)
subprocess.run('docker stop instagram', shell=True)

subprocess.run(
    'docker run {options} {tag}'.format(
        options=' '.join([
            f'{key} {value}' for key, value in DOCKER_OPTIONS
        ]),
        tag=DOCKER_IMAGE_TAG
    ), shell=True
)
