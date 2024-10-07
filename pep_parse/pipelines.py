import csv
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_count.values())
        self.status_count['Total'] = total

        formatted_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = BASE_DIR / f'results/status_summary_{formatted_time}.csv'
        os.makedirs('results', exist_ok=True)

        with open(filename, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])

            writer.writerows(self.status_count.items())

