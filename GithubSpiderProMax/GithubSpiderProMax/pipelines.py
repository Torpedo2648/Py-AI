# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd

class GithubspiderpromaxPipeline:
    def open_spider(self, spider):
            self.df = pd.DataFrame()

    def close_spider(self, spider):
        self.df.sort_values(by="stars", ascending=False, inplace=True)
        self.df.to_csv("info7.csv")

    def process_item(self, item, spider):
        item = pd.Series(item)
        self.df = pd.concat([self.df, item.to_frame().T], ignore_index=True)
        return item