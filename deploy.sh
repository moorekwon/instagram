#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/wps12th.pem"
HOST="ubuntu@13.125.213.68"
ORIGIN_SOURCE="$HOME/projects/wps12th/instagram"
DEST_SOURCE="/home/ubuntu/projects/instagram"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${HOST}"

echo "== runserver 배포 =="
# 기존 폴더 삭제
echo "1. 기존 폴더 삭제"
${SSH_CMD} sudo rm -rf S{DEST_SOURCE}
#ssh -i ~/.ssh/wps12th.pem ubuntu@13.125.213.68 rm -rf /home/ubuntu/projects/instagram

# 로컬에 있는 파일 업로드
echo "2. 로컬 파일 업로드"
scp -q -i "${IDENTITY_FILE}" -r "${ORIGIN_SOURCE}" ${HOST}:${DEST_SOURCE}
#scp -i ~/.ssh/wps12th.pem -r ~/projects/wps12th/instagram ubuntu@13.125.213.68:/home/ubuntu/projects/

echo "3. Screen 실행"
# 실행중이던 screen 세션 종료
${SSH_CMD} -C 'screen -X -S runserver quit'
#ssh -i ~/.ssh/wps12th.pem ubuntu@13.125.213.68 -C 'screen -X -S runserver quit'

# screen 실행
${SSH_CMD} -C 'screen -S runserver -d -m'
#ssh -i ~/.ssh/wps12th.pem ubuntu@13.125.213.68 -C 'screen -S runserver -d -m'

# 실행중인 세션에 명령어 전달
${SSH_CMD} -C "screen -r runserver -X stuff $'sudo python3 /home/ubuntu/projects/instagram/app/manage.py runserver 0:80\n'"
#ssh -i ~/.ssh/wps12th.pem ubuntu@13.125.213.68 -C "screen -r runserver -X stuff $'sudo python3 /home/ubuntu/projects/instagram/app/manage.py runserver 0:80\n'"

echo "== 배포 완료 =="