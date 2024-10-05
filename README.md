# Как запустить проект.
### **Клонировать репозиторий и перейти в него в командной строке:**
```python 
  git clone git@github.com:SkullPiercer/scrapy_parser_pep.git
```
```python
  cd scrapy_parser_pep
```
### **Cоздать и активировать виртуальное окружение:**
#### Windows:
```python
  python -m venv venv
```
```python
  source venv/Scripts/activate
```
#### Linux/Mac:
```python
  python3 -m venv env
```
```python
  source env/bin/activate
```
### **Установить зависимости из файла requirements.txt:**
#### Windows:
```python
  python -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
#### Linux/Mac
```python
  python3 -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```

### **Запустить парсер:**
```python
  scrapy crawl pep
```