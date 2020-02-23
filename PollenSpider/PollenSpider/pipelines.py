# -*- coding: utf-8 -*-
import psycopg2
import datetime


class PollenspiderPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'wolf330312'
        database = 'pollendb'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        date = datetime.datetime.strptime(item['date'], "%d.%m.%Y.").date()
        self.cur.execute('INSERT INTO pollen(name,level_text,level,city,date) values(%s,%s,%s,%s,%s)',
                         (item['name'], item['level-text'], item['level'], item['city'], date))
        self.connection.commit()
        return item
