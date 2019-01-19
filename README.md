# Docker-nginx-php-fpm-xDebug
1) git clone this
2) Открыть в новом окне скачанный проект
![image](https://user-images.githubusercontent.com/39625189/51432752-dd28aa00-1c4d-11e9-9c03-0db9b855c6b6.png)
3) Настройки File | Settings | Build, Execution, Deployment | Docker
![image](https://user-images.githubusercontent.com/39625189/51432794-b9b22f00-1c4e-11e9-81e9-00d0ef6c8f5a.png)
4) Настройки File | Settings | Languages & Frameworks | PHP
  1 - выбираем версию языка
  2 - жмем три точки
![image](https://user-images.githubusercontent.com/39625189/51432819-334a1d00-1c4f-11e9-945f-afb79020e812.png)
Откроется окно жмем плюсик
![image](https://user-images.githubusercontent.com/39625189/51432861-e7e43e80-1c4f-11e9-8a63-8bc38549f16b.png)
Далее жмем FROM Docker...<br>
![image](https://user-images.githubusercontent.com/39625189/51432885-56290100-1c50-11e9-8b22-8c21efd58975.png)
В открывшемся окне выбираем Docker Compose, путь к файлу docker-compose.yml. Service сами подтянутся автоматически после выбора docker-compose.yml.
Выбираем из выпадающего списка php-fpm для Service.
![image](https://user-images.githubusercontent.com/39625189/51432900-c041a600-1c50-11e9-8ab9-bde0384e7e26.png)
