FROM php:7.4-fpm

RUN apt-get update \
# установка xdebug
&& pecl install xdebug \
# включение xdebug
&& docker-php-ext-enable xdebug \
&& docker-php-ext-install pdo

WORKDIR /var/www