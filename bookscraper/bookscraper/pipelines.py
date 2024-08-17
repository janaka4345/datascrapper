# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        # print(spider)
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if adapter.get(field_name) == False:
                adapter[field_name] = True
            print(f"{field_name}--------{adapter.get(field_name)}")

        return item
