# Yandex translator

Simple Yandex translator in Python.<br>
Requirements:<br>
  + Library **requests**<br>
  + Requirements: getting API-KEY on https://tech.yandex.com/translate/<br>
Thanks for the idea [Nikita Vandishev](https://gist.github.com/nekitvand).<br>

Простой яндекс переводчик на Python.<br>
Требования:<br>
  + Библиотека **requests**<br>
  + Получение API-KEY на https://tech.yandex.com/translate/<br>
Благодарность за идею [Nikita Vandishev](https://gist.github.com/nekitvand)<br>

Example:
```shell
$ python yatrans.py ru-en "Я яндекс-переводчик"
I Yandex-translator
```

File [yatrans.sh](https://github.com/delvin-fil/yatrans/blob/master/yatrans.sh) designed for installation of "mediator" between the script and the DE/WM in Linux and creating combinatii keys.

Файл [yatrans.sh](https://github.com/delvin-fil/yatrans/blob/master/yatrans.sh) предназначен для установки "посредником" между скриптом и DE/WM Linux и создании комбинкации клавиш. 

Example for IceWM:

```shell
$ export PATH="${PATH}:$HOME/.local/bin"
$ chmod +x path/to/yatrans.py
$ chmod +x path/to/yatrans.sh

$ ln -s path/to/yatrans.py $HOME/.local/bin/mytrans
$ nano $HOME/.icewm/keys
# add string
key "Ctrl+1" path/to/yatrans.sh
............
```
