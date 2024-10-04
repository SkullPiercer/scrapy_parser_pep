import csv
import os
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

class PepParsePipeline:
    def __init__(self):
        self.status_count = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            if status in self.status_count:
                self.status_count[status] += 1
            else:
                self.status_count[status] = 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_count.values())
        formatted_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = BASE_DIR / f'results/status_summary_{formatted_time}.csv'

        os.makedirs('results', exist_ok=True)

        with open(filename, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])

            for status, count in self.status_count.items():
                writer.writerow([status, count])

            writer.writerow(['Total', total])
