# engineering_practices
Homeworks for engineering practices. HSE, 2023.

#HW2

Инструмент для версионирования данных, который будет использоваться в данной работе: LFS (Git Large File Storage)

Скачиваем инструмент: `sudo apt-get install git-lfs`, `git lfs install`.

Добавляем трекинг файлов с расширением `.csv`: `git lfs track "*.csv"`
В папке появляется файл: `.gitattributes` 

Проверить какие файлы версионируются: `git lfs ls-files` или `git status`.


Добавить файлы на GitHub: `git add some_file.csv`, `git commit -m "hw2"`, `git push origin main`

Обновлять файлы - изменять локально, делать коммит. Вернуться к первоначальной версии с гита: `git reset --hard origin/main`.

Получить данные: `git clone https://github.com/sunnysea/engineering_practices.git`

