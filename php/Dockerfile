FROM php:7.4-fpm

RUN apt-get update \
# установка xdebug
&& pecl install xdebug \
# включение xdebug
&& docker-php-ext-enable xdebug \
&& docker-php-ext-install pdo \
# установка COMPOSER
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www