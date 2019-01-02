from data_collection.collector import Collector

if __name__ == '__main__':
    collector = Collector()

    html = collector.simple_get('https://www.babycenter.com.au/g25001383/expecting-a-baby-')

    print(html)
