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

 - C:\Users\VED>mkvirtualenv as
 - (as) C:\Users\%User>
 - *подробности по установке http://docs.python-guide.org/en/latest/dev/virtualenvs/
 - git clone https://github.com/mirjalolbahodirov/bozor.git
2) Сделать запрос командой pip install -r requirements\base.txt
3) Сделать миргацию  если работаете через командную строку нужно прописать  python manage.py migrate
(Убедитесь что находитесь в проекте под названием bozor)
- У вас должно выглядить вот так:
- (as) C:\Users\VED\Desktop\bozor>python manage.py makemigrations
-No changes detected

-(as) C:\Users\VED\Desktop\bozor>python manage.py migrate
-Operations to perform:
-  Apply all migrations: admin, auth, contenttypes, sessions, shop
-Running migrations:
-  No migrations to apply.

- (as) C:\Users\VED\Desktop\bozor>
4) И ввести ваше данные из Postgresql БД.
