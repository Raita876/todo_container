FROM mysql:5.7

RUN mkdir -p /var/log/mysql/ && touch /var/log/mysql/mysqld.log

ADD ./init/sample.sql /docker-entrypoint-initdb.d
ADD ./my.conf /etc/mysql/conf.d/mysql.cnf

CMD ["mysqld", "--character-set-server=utf8", "--collation-server=utf8_unicode_ci"]
