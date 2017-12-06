# bozor 
 Это проект находиться в стадии тестирования. 
1) Для того чтобы установить нужно установить набираете в командной строке внутри Virtual Environment 
 - pip install virtualenv 
 - * Убедитесь что у вас последняя версия 
 - virtualenv --version
 - pip install virtualenvwrapper & pip install virtualenvwrapper-win
 * Virtual Environment можно создать командой:
 - mkvirtualenv my_project
 - *Убедитесь что у вас всё создалось успешно и вы находитесь в Virtual Environment
 - *должно выглядить вот так
 Microsoft Windows [Version 6.1.7601]
(c) Корпорация Майкрософт (Microsoft Corp.), 2009. Все права защищены.

 - C:\Users\VED>mkvirtualenv my_project
 - (as) C:\Users\%User>
 - *подробности по установке http://docs.python-guide.org/en/latest/dev/virtualenvs/
 - git clone https://github.com/mirjalolbahodirov/bozor.git
2) Сделать запрос командой pip install -r requirements\base.txt
3) Сделать миргацию managa.py makemigrations и managy.py migrate
4) И ввести ваше данные из Postgresql БД.
