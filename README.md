# engineering_practices
Homeworks for engineering practices. HSE, 2023.

Мной был взят для форматирования питоновский файл, в котором находится домашнее задание для одного из предметов.

Установка:

`pip install poetry`

`poetry new hw1`

`cd .\hw1\`

`poetry add --dev black ruff isort`

Тут возникла проблема с версией питона, и я очень много времени потеряла на установке версии 3.10. Изначально у меня была версия 3.7.

`poetry add numpy`

`poetry lock`

Развертывание окружения: `poetry shell`

Возникла ошибка `*Невозможно загрузить файл C:\Users\Pauline_Shuvalova\AppData\Local\pypoetry\Cache\virtualenvs\hw1-wue8-cNQ-py3.10\Scrip
ts\activate.ps1, так как выполнение сценариев отключено в этой системе. Для получения дополнительных сведений см. about
_Execution_Policies по адресу https:/go.microsoft.com/fwlink/?LinkID=135170.
    + CategoryInfo          : Ошибка безопасности: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnauthorizedAccess*`
Потом я ее как-то починила, как и версию питона.


`poetry build`

Итого форматирование кода:

- `poetry run black Task_1.py`
- `poetry run flake8 Task_1.py`
- `poetry run pylint Task_1.py`

![image](https://github.com/sunnysea/engineering_practices/assets/78918468/c2643ee4-3cfc-40fc-85cc-a00990be304f)
