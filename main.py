from etherscan import Etherscan
from openpyxl import Workbook, load_workbook
import csv
from datetime import datetime
from variable import *

"""

holders = {}

YOUR_API_KEY = '7HZJFYIG6XT58SP3VWU49NJJ3FSRHP23H6'

eth = Etherscan(YOUR_API_KEY)


wb_coin_addresses = load_workbook('CoinAdresses.xlsx')
ws_coin_adresses = wb_coin_addresses.active

wb_new = load_workbook(yfi_holders_file) #change here!!!!
ws_new = wb_new.active


def get_holders_from_csv_file(file_holders_etherscan):
    with open(file_holders_etherscan) as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            try:
                holders[line[0]] = int(float(line[1]))
            except ValueError:
                do_nothing = 1

        sort_holders = sorted(holders.items(), key = lambda x:x[1], reverse= True)

        return sort_holders


def write_holders_in_addresses_file(holders_f, ind, coin_name):
    row_index = chr(64 + ind)
    ws_coin_adresses[row_index + '1'].value = coin_name


    for i in range (99):
        cell = row_index + str(i + 2)
        ws_coin_adresses[cell] = holders_f[i][0]


def write_holders_data_in_day_tracker(ind):
    row_index = chr(64 + ind)
    cnt = 1


    for row_cells in ws_new.iter_cols(min_row=1, max_row=1, max_col=99):
        cnt += 1
        for cell in row_cells:
            cell.value = str(ws_coin_adresses[row_index + str(cnt)].value)



def write_daily_account_balance(day):
    row_index = chr(64 + day)

    cnt = 1

    for row_cells, row_cells1 in zip(ws_new.iter_cols(min_row=day, max_row=day),  ws_new.iter_cols(min_row=1, max_row=1)):
        cnt += 1
        for cell, cell1 in zip(row_cells, row_cells1):
            print(cnt)
            if cnt < 100:
                cell.value = eth.get_acc_balance_by_token_and_contract_address(yfi, cell1.value)   #change here


def main():
    holders_f = get_holders_from_csv_file(yfi_file)  #takes from the exported holders files from etherscan.io of a coin the first 100 holcers by quantity               #change here

    index_row = 25      #change this
    write_holders_in_addresses_file(holders_f, index_row, 'Yfi')    #writes the top 100 holders of the coin in the coinaddresses.xlsx           # CANGE HERE!!!!! index and name
    #
    write_holders_data_in_day_tracker(index_row)   #write the in the first row the top 100 holders

    day_of_the_year = datetime.now().timetuple().tm_yday - 10 #change to 8

    write_daily_account_balance(day_of_the_year) #emits query based on the holder and writes it down based on the DAY!!!!

    wb_new.save(yfi_holders_file)    #change   here
    wb_coin_addresses.save('CoinAdresses.xlsx')


if __name__ == "__main__":
    main()




"""
