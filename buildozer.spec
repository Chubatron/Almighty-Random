[app]

# Название приложения
title = Almighty Random

# Пакетное имя
package.name = almightyrandom
package.domain = org.yourdomain

# Версия приложения
version = 1.0.0

# Описание
description = Magic ball, coin, dice, roulette and more random games

# Основной файл приложения
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ogg,mp3,json,ttf

# Требования (библиотеки) - ИСПРАВЛЕННАЯ ВЕРСИЯ БЕЗ ОШИБКИ long
requirements = python3,kivy==2.3.0,Pillow,numpy,android,requests,pyjnius==1.5.0,cython==0.29.37

# Имя класса App
app.class = SportsGameApp

# Ориентация экрана
orientation = portrait

# Иконка приложения
# icon.filename = %(source.dir)s/assets/icon.png

# Заставка при запуске
# presplash.filename = %(source.dir)s/assets/presplash.png

# Цвет заставки
presplash.color = 0.1, 0.1, 0.1, 1

# Разрешения для Android
android.permissions = INTERNET, VIBRATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Минимальная версия Android (API 21 = Android 5.0)
android.minapi = 21

# Целевая версия Android
android.targetsdk = 33

# Архитектуры процессора
android.archs = arm64-v8a

# Автоматическое принятие лицензий SDK
android.accept_sdk_license = True

# Полноэкранный режим
fullscreen = 1

# Уровень логгирования
log_level = 2

# Папка для сборки
build_dir = .buildozer

# Кэш
cache_dir = .buildozer/cache