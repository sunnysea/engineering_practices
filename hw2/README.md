# engineering_practices
Homeworks for engineering practices. HSE, 2023.

#HW2

Инструмент для версионирования данных, который будет использоваться в данной работе: *LFS (Git Large File Storage)*

(Данные взяты из одной из лабораторных работ в ВШЭ.)

- Скачиваем инструмент: 
`sudo apt-get install git-lfs`, `git lfs install`.

- Добавляем трекинг всех файлов с расширением .csv: `git lfs track "*.csv"`
    В папке появляется файл: `.gitattributes` 

- Проверить какие файлы версионируются: `git lfs ls-files` или `git status`.

- Добавить файлы на GitHub: `git add some_file.csv`, `git commit -m "hw2"`, `git push origin main`
  
#### Инструкция для работы с инструментом:

Добавлять, обновлять файлы: изменять локально, делать коммит, как описано было выше. 

Вернуться к первоначальной версии с гита: `git reset --hard origin/main`.

Получить данные и воспроизводить дальше локально: `git clone https://github.com/sunnysea/engineering_practices.git`

