import datetime


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%dT%H-%M-%S")
FEEDS = {
    f'results/pep_{formatted_time}.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
