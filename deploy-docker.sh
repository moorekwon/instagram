#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/nuna.pem"
USER="ubuntu"
HOST="15.164.95.164"
TARGET=${USER}@${HOST}
ORIGIN_SOURCE="$HOME/projects/wps12th/instagram/"
DOCKER_REPO="raccoonhj33/200128-instagram"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${TARGET}"

echo "== Docker 배포 =="

# 서버 초기설정
echo "apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTED=noninteractive apt dist-upgrade -y && apt -y autoremove'

echo "apt install docker.io"
${SSH_CMD} -C 'sudo apt -y install docker.io'

# pip freeze
echo "pip freeze"
"$HOME"/.pyenv/versions/wps-instagram-env/bin/pip freeze >"${ORIGIN_SOURCE}"requirements.txt

# docker build
# 1. poetry export를 사용해서 requirements.txt를 생성
#   > dev 패키지는 설치하지 않도록 함 (공식문서 또는 사용법 참고)
echo "poetry export"
poetry export -f requirements.txt >requirements.txt

echo "docker build"
docker build -q -t ${DOCKER_REPO} -f Dockerfile "${ORIGIN_SOURCE}"

# docker push
echo "docker push"
docker push ${DOCKER_REPO}

echo "docker stop"
${SSH_CMD} -C 'sudo docker stop instagram'

echo "docker pull"
${SSH_CMD} -C "sudo docker pull ${DOCKER_REPO}"

# 로컬의 aws profile 전달
scp -q -i "${IDENTITY_FILE}" -r "$HOME/.aws/" ${TARGET}:/home/ubuntu/

# screen에서 docker run
echo "screen settings"
# 실행 중이던 screen 세션 종료
${SSH_CMD} -C 'screen -X -S docker quit'
# screen 실행
${SSH_CMD} -C 'screen -S docker -d -m'
# 실행 중인 screen에서 docker container을 사용해서 bash 실행
${SSH_CMD} -C "screen -r docker -X stuff 'sudo docker run --rm -it -p 80:8000 --name=instagram ${DOCKER_REPO} /bin/bash\n'"
# bash를 실행 중인 container에 HOST의 ~/.aws 폴더를 복사
${SSH_CMD} -C "sudo docker cp ~/.aws/ instagram:/root"
# container에서 bash를 실행 중인 screen에 runserver 명령어를 전달
${SSH_CMD} -C "screen -r docker -X stuff 'python manage.py runserver 0:8000\n'"

echo "== Docker 배포 완료 =="
