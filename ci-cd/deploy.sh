#!/bin/bash

# Данные для подключения
USER=pi
HOST=192.168.1.100
PROJECT_PATH=/home/pi/greenhouse_project

echo "[CI/CD] 🔄 Начало деплоя на Raspberry Pi"

# Копирование сервера
scp -r server/* $USER@$HOST:$PROJECT_PATH/server/

# Перезапуск systemd-сервиса (если используется)
ssh $USER@$HOST << EOF
    cd $PROJECT_PATH/server
    sudo systemctl restart greenhouse.service
EOF

echo "[CI/CD] ✅ Деплой завершён успешно"
