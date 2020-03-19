FROM php:7.4-fpm

RUN apt-get update \
&& apt-get install python3 -y \
# установка xdebug
&& pecl install xdebug \
# включение xdebug
&& docker-php-ext-enable xdebug \
&& docker-php-ext-install pdo \
# установка COMPOSER
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
&& apt-get install git -y

COPY ./php/script/ /var/script/
# установка user.name + user.email. Экстендит базовый CMD (php-fpm) образа
#CMD sudo python3 /var/script/setgitoptions.py && php-fpm
CMD php-fpm
WORKDIR /var/www
