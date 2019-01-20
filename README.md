# Docker-nginx-php-fpm-xDebug
## Инструкция:
### 1) Клонируем репозиторий git clone
### 2) Открыть в новом окне скачанный проект
![image](https://user-images.githubusercontent.com/39625189/51432752-dd28aa00-1c4d-11e9-9c03-0db9b855c6b6.png)
### 3) Настройки File | Settings | Build, Execution, Deployment | Docker
![image](https://user-images.githubusercontent.com/39625189/51432794-b9b22f00-1c4e-11e9-81e9-00d0ef6c8f5a.png)
### 4) Настройки File | Settings | Languages & Frameworks | PHP
  1 - выбираем версию языка
  2 - жмем три точки<br>
![image](https://user-images.githubusercontent.com/39625189/51432819-334a1d00-1c4f-11e9-945f-afb79020e812.png)
<br>Откроется окно жмем плюсик<br>
![image](https://user-images.githubusercontent.com/39625189/51432861-e7e43e80-1c4f-11e9-8a63-8bc38549f16b.png)
<br>Далее жмем FROM Docker...<br>
![image](https://user-images.githubusercontent.com/39625189/51432885-56290100-1c50-11e9-8b22-8c21efd58975.png)
<br>В открывшемся окне выбираем Docker Compose, путь к файлу docker-compose.yml. Service сами подтянутся автоматически после выбора docker-compose.yml.<br>
Выбираем из выпадающего списка php-fpm для Service.<br>
![image](https://user-images.githubusercontent.com/39625189/51432900-c041a600-1c50-11e9-8ab9-bde0384e7e26.png)
<br>Жмем ОК после чего должно получиться следующее:<br>
![image](https://user-images.githubusercontent.com/39625189/51433485-19630700-1c5c-11e9-891b-99b03db526db.png)
<br>Жмем apply и видим<br>
![image](https://user-images.githubusercontent.com/39625189/51433504-9d1cf380-1c5c-11e9-94de-c3ab12750c90.png)
<br>Жмем apply и сворачиваем настройки<br>
<br>Переходим public/index.php ставим брекпоинт и включаем прослушку дебагера<br>
![image](https://user-images.githubusercontent.com/39625189/51433536-698e9900-1c5d-11e9-9f95-6904ee4eb72c.png)
<br>В /etc/hosts своей локальной машины НЕ КОНТЕЙНЕРА добавляем сайты из www<br>
![image](https://user-images.githubusercontent.com/39625189/51433553-094c2700-1c5e-11e9-801b-2cd6870a880f.png)
<br>Делаем запрос в браузере,postman и т.д к нашему сайту test1.local<br>
Видим что скрипт не завершил свою работу<br>
![image](https://user-images.githubusercontent.com/39625189/51433593-97281200-1c5e-11e9-809c-cd3b6c9809d8.png)
<br>После чего в PhpStorm откроется окно<br>
![image](https://user-images.githubusercontent.com/39625189/51433574-63e58300-1c5e-11e9-9c15-baa5456f011a.png)
<br>Жмем ОК и видим работающий xDebug<br>
![image](https://user-images.githubusercontent.com/39625189/51433597-c8a0dd80-1c5e-11e9-83a2-84288f98e14b.png)
<br>Также после того как мы нажали ОК у нас в настройках будет создан следующий "Server"<br>Где слева путь к файлу на локальной машине, а справа его расположение в докер-контейнере. <b>Этот момент важен!!!</b> В нашем случае все выставилось автоматически. Также можно самому создавать "сервера" и выставлять соотвествия папок (без этого маппинга работать дебагер не будет).<br>Символ **_** обозначает любой сервер. 
![image](https://user-images.githubusercontent.com/39625189/51433632-179b4280-1c60-11e9-901a-c92362b77a64.png)
В общем-то все.<br>Но еще можно добавить возможность запуска bash:<br>
Жмем на Docker в нижем левом углу, выбираем наш контейнер с php-fpm, жмем правой кнопкой мыши на него и выбираем exec.
<br>Жмем create и видим окошко в котором вводим bash и жмем ОК.<br>
![image](https://user-images.githubusercontent.com/39625189/51433751-87123180-1c62-11e9-9b06-ce8be0705df7.png)
<br>После чего октрывается bash нашего контейнера, где можно делать что угодно, но не стоит забывать что после пересборки все изменения пропадут(расшаренные файлы не в счет).<br>
![image](https://user-images.githubusercontent.com/39625189/51433758-ac06a480-1c62-11e9-84ae-74333b5a4140.png)
