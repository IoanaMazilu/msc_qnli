micro_tron_price_premise = 36
dynaco_price_premise = 48
total_shares = 300
average_price_per_share = 40

# the hypothesis talks about the price of the same stocks, but in a different scenario
# the premise scenario is used to calculate the number of shares of Dynaco stock sold
dynaco_shares_sold_premise = total_shares * (dynaco_price_premise / average_price_per_share)

# the hypothesis scenario is different from the premise scenario
# therefore, the hypothesis cannot be entailed from the premise
label = "contradiction"

print(label)
