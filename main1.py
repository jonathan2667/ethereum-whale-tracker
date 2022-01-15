from etherscan import Etherscan
from openpyxl import Workbook, load_workbook
import csv
from datetime import datetime
from variable_dic import *
import sys
from requests import Request, Session
import json
import pprint
from termcolor import colored


YOUR_API_KEY = '7HZJFYIG6XT58SP3VWU49NJJ3FSRHP23H6'

eth = Etherscan(YOUR_API_KEY)


def write_daily_account_balance(day, ws_new, name):
    row_index = chr(64 + day)

    cnt = 1

    for row_cells, row_cells1 in zip(ws_new.iter_cols(min_row=day, max_row=day),  ws_new.iter_cols(min_row=1, max_row=1)):
        cnt += 1
        for cell, cell1 in zip(row_cells, row_cells1):
            print(cnt)
            if cnt < 100:
                cell.value = eth.get_acc_balance_by_token_and_contract_address(name, cell1.value)   #change here


def do_for_all_25_upddates():
    index = 0
    ok = 0
    for key, value in dic_var.items():
        index = index + 1

        if 'holders' in key:
            print(value)
            day_of_the_year = datetime.now().timetuple().tm_yday - 10

            wb_new = load_workbook(value)
            ws_new = wb_new.active

            coin_name = list(dic_var.items())[index - 2][1]

            write_daily_account_balance(day_of_the_year, ws_new, coin_name)

            wb_new.save(value)

def travel_over_data(ws_new):
    day = datetime.now().timetuple().tm_yday - 10

    portfolios_that_added = 0
    portfolios_that_sold = 0
    portfolios_no_action = 0
    volume_total_top_holders = 0
    cvd_top_holders = 0

    row_index = chr(64 + day)

    cnt = 1

    for row_cells, row_cells1 in zip(ws_new.iter_cols(min_row=day, max_row=day), ws_new.iter_cols(min_row=day-1, max_row=day-1)):
        cnt += 1
        for cell, cell1 in zip(row_cells, row_cells1):
            if cnt < 100:
                if cell.value > cell1.value :
                    portfolios_that_added = portfolios_that_added + 1
                elif cell.value < cell1.value:
                    portfolios_that_sold = portfolios_that_sold + 1
                else:
                    portfolios_no_action = portfolios_no_action + 1
                volume_total_top_holders = volume_total_top_holders + abs((int(float(cell.value))/1000000000000000000 - int(float(cell1.value))/1000000000000000000))
                cvd_top_holders = cvd_top_holders + (int(float(cell.value))/1000000000000000000 - int(float(cell1.value))/1000000000000000000)

    volume_total_top_holders = round(volume_total_top_holders, 2)

    return volume_total_top_holders, round(cvd_top_holders, 2),  portfolios_that_added, portfolios_that_sold, portfolios_no_action

def analysis():

    index = 0
    index_till_25 = 0

    for key, value in dic_var.items():
        index = index + 1

        if 'holders' in key:
            color = ''

            index_till_25 = index_till_25 + 1

            coin_name = list(dic_var.items())[index - 2][0]
            print(coin_name)

            wb_new = load_workbook(value)
            ws_new = wb_new.active

            volume_top_holders, cvd_top_holders, portfolios_that_added, portfolios_that_sold, portfolios_no_action = travel_over_data(ws_new)
            curr_price, percent_change_24h, overall_volume_change_24h, volume_24h = crypto(list_symbol[index_till_25 - 1])

            if portfolios_that_sold > portfolios_that_added:
                color = 'red'
            elif portfolios_that_sold < portfolios_that_added:
                color = 'green'
            else:
                color = 'white'

            print(list_symbol[index_till_25 - 1])
            print(colored(" THE TOP HOLDERS VOLUME IS : ", color), colored(volume_top_holders * curr_price, color), colored(" CVD OF TOP HOLDERS: ", color), colored(cvd_top_holders, color), colored(" ADDED: ", color), colored(portfolios_that_added, color), colored("   SOLD: ", color), colored(portfolios_that_sold, color), colored( "    NULL:", color), colored(portfolios_no_action, color))
            print(colored(" VOLUME 24h: ", color), colored(volume_24h, color) , colored("   CURRENT PRICE: ", color), colored(curr_price, color), colored("  PERCENT CHANGE: ", color), colored(percent_change_24h, color), colored('%', color), colored("   OVERALL VOLUME 24 H: ", color) , colored(overall_volume_change_24h, color), colored("%", color))

            print('')


def crypto(coin_name) :
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol' : coin_name,
        'convert' : 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'db843e5d-7d82-4e93-8f59-402955688290'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    curr_price = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['price'], 2)
    percent_change_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['percent_change_24h'], 2)
    overall_volume_change_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['volume_change_24h'], 2)
    volume_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['volume_24h'], 2)

    #pprint.pprint(json.loads(response.text))

    return  curr_price, percent_change_24h, overall_volume_change_24h, volume_24h


def main():
    # do_for_all_25_upddates()
    analysis()




if __name__ == "__main__":
    main()




