from etherscan import Etherscan
from openpyxl import Workbook, load_workbook
import csv

holders = {}

serum_file = 'export-tokenholders-for-contract-0x476c5E26a75bd202a9683ffD34359C0CC15be0fF.csv'
serum = "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff"
serum_holders_file = 'SerumHolders.xlsx'

YOUR_API_KEY = 'myapikey'

eth = Etherscan(YOUR_API_KEY)

wb_coin_addresses = load_workbook('CoinAdresses.xlsx')
ws_coin_adresses = wb_coin_addresses.active

wb_serum = load_workbook(serum_holders_file)
ws_serum = wb_serum.active


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
    ws_coin_adresses['A1'].value = coin_name
    row_index = chr(64 + ind)

    for i in range (99):
        cell = 'A' + str(i + 2)
        ws_coin_adresses[cell] = holders_f[i][0]


def write_holders_data_in_day_tracker():
    cnt = 1

    for row_cells in ws_serum.iter_cols(min_row=1, max_row=1):
        cnt += 1
        for cell in row_cells:
            cell.value = str(ws_coin_adresses['A' + str(cnt)].value)


def write_daily_account_balance(day):
    row_index = chr(64 + day)

    cnt = 1

    for row_cells, row_cells1 in zip(ws_serum.iter_cols(min_row=day, max_row=day),  ws_serum.iter_cols(min_row=1, max_row=1)):
        cnt += 1
        for cell, cell1 in zip(row_cells, row_cells1):
            if cnt < 100:
                cell.value = eth.get_acc_balance_by_token_and_contract_address(serum, cell1.value)


def main():
#     holders_f = get_holders_from_csv_file(serum_file)  #takes from the exported holders files from etherscan.io of a coin the first 100 holcers by quantity
#
#     write_holders_in_addresses_file(holders_f, 1, 'Serum')    #writes the top 100 holders of the coin in the coinaddresses.xlsx
#
#     write_holders_data_in_day_tracker()   #write the in the first row the top 100 holders

#    write_daily_account_balance(2) #emits query based on the holder and writes it down

    wb_serum.save(serum_holders_file)
    wb_coin_addresses.save('CoinAdresses.xlsx')

if __name__ == "__main__":
    main()




