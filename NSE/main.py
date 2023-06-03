from nse import NSE

class StockPrice:
    def __init__(self, stock_name, stock_index='nse'):
        self.stock_name = stock_name.strip()
        self.stock_index = stock_index.strip().lower()
        if self.stock_index == 'nse':
            print(f'Searching for {self.stock_name} nse stock...')
            self.stock = NSE(stock_name)
            self.stock_name = self.stock.stock_name
            print(f'Found stock based on provided name: {self.stock_name}\nStock instance created')
        else:
            print(f'{self.stock_index} stock scraping code under development.\nPlease wait for Update.')

    
    def get_latest_price(self):
        return self.stock.get_latest_price()

    def get_historical_data(self, from_date, to_date):
        return self.stock.get_historical_data(from_date, to_date)
    

if __name__ == "__main__":
    # stock name
    infosys_stock = StockPrice('','nse')
    latest_price_info = infosys_stock.get_latest_price()
    # start date and end date
    historical_price_info = infosys_stock.get_historical_data('', '')
    print(latest_price_info)
    print(historical_price_info)
