# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl


class QuotespiderPipeline:
    # def open_spider(self, spider):
    #     self.wb = openpyxl.Workbook()
    #     self.ws = self.wb.active
    #     self.ws.title = 'Authors&Quotes'
    #     self.ws.append(['author', 'text', 'tags', 'name', 'born_date', 'born_location','description'])
    #  
    # def close_spider(self, spider):
    #     self.wb.save('quotes.xlsx')

    def process_item(self, item, spider):
        # author = item.get('author', '')
        # text = item.get('text', '')
        # tags = str(item.get('tags', ''))
        # name = item.get('name', '')
        # born_date = item.get('born_date', '')
        # born_location = item.get('born_location', '')
        # description = item.get('description', '')
        # self.ws.append([author, text, tags, name, born_date, born_location, description])
        return item
