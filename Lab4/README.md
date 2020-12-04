### Lab4
1. Ознайомився з Docker.
2. Виконав команди:
    - "sudo docker -v"
    - "sudo docker -h"
    - "sudo docker run docker/whalesay cowsay Docker is fun"
    - Перенаправив вивід в my_work.log:
        - "sudo docker -v > my_work.log && sudo docker -h >> my_work.log && sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log"
3. Ознайомився з документацією
4. - Виконав команди:
        - "sudo docker pull python:3.7-slim"
        - "sudo docker images"
        - "sudo docker inspect python:3.7-slim"
    - Створив файл з іменем Dockerfile скопіював туди вміст такого ж файлу з репозиторію;
    - Ознайомився із коментарями;
    - Замінив посилання на власний Git репозиторій із веб-сайтом та закомітив даний Dockerfile*
5. Створив власний репозиторій на Docker Hub
6. Виконав команди:
    - "sudo docker build -t oleh000voloshchuk/tpis:django ."
    - "sudo docker images"
    - "sudo docker push oleh000voloshchuk/tpis:django"
    - [repo](https://hub.docker.com/repository/docker/oleh000voloshchuk/tpis)
    - [image](https://hub.docker.com/layers/128622823/oleh000voloshchuk/tpis/django/images/sha256-e5f73b97bcb9d8b87161d2ab04fc704221c4ebf286592a9cde0e636585040bbf?context=explore)
7. Виконав команду:
    - "sudo docker run -it --rm -p 8000:8000 oleh000voloshchuk/tpis:django"
    - Веб-сайт працює
8. Домашня робота:
    - створив Dockerfile.monitor
    - Виконав білд імеджа (я зробив спеціально для цього інший репозиторій в Докері, але тільки тепер зрозумів, що його можна було робити в тому самому репозиторії)
        - "sudo docker build -t oleh000voloshchuk/mon:monitoring ."
        - "sudo docker images"
        - "sudo docker push oleh000voloshchuk/mon:monitoring "
        - [repo](https://hub.docker.com/repository/docker/oleh000voloshchuk/mon)
        - [image](https://hub.docker.com/layers/128635345/oleh000voloshchuk/mon/monitoring/images/sha256-ee6080e8a88ef37e830780d299babf711a605b353cd22db2edf7a92c3ae84dc3?context=explore)
    - Виконав команди:
        - "sudo docker run -it --rm -p 8000:8000 oleh000voloshchuk/tpis:django"
        - "sudo docker run --net=host -it --rm  8000:8000 oleh000voloshchuk/mon:monitoring"
    - Виконав команди:
        - "sudo docker ps"
        - "sudo docker export b8f6c03865cb > latest.tar"
    - Витягнув з архіву server.log
