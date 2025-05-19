Начнем с установки uv - оно удобно:

sudo apt install -y curl - ну если не установлено
curl -LsSf https://astral.sh/uv/install.sh | sh - установка “uv” (не забываем sudo)

Далее, открываем директорию(пустую папку) через терминал:
git clone https://github.com/Max1muth/pure_project.git

cd pure_project - переход в директрию, в которой будет виртуальное окружение

ls - я обычно смотрю, точно ли скачалось все, лишний раз перестраховка

uv venv .venv --python=$(cat python-version.txt | cut -d' ' -f2) && source .venv/bin/activate - лучше почитать, но в общем uv создает виртуальное окружение которому приписывается название .venv,
--python=$(cat python-version.txt | cut -d' ' -f2) - эта часть берет файл python-version.txt, и | cut -d' ' -f берет из файла только цифры версии и устанавливает, после окружениие активируется

ls -la - показывает скрытые файлы в том числе, то есть .venv

uv pip install -r requirements.txt --python .venv/bin/python - читает файл с библиотеками

uv pip list - соответственно работает если выводит (если запуск каких-то файлов говорит, что модуль не установлен - uv pip install <...>)


Можно запускать последовательно creating_data.py, dataframe.py, preprocessing.py (файлы data пересоздаются)
Можно просто вызвать preprocessing.py
