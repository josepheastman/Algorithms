#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = -10
    buy_price = 0
    sell_price = 0

    buy_index = True

    for i in range(0, len(prices)-1):
        sell_price = prices[i+1]

        if buy_index:
            buy_price = prices[i]

        if sell_price < buy_price:
            buy_index = True
            continue
        else:
            temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit
            buy_index = False
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
