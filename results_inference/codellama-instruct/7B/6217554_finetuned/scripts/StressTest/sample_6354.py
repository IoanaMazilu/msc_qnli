microtron_stock_premise = 36
dynaco_stock_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_stock_hypothesis = 76
dynaco_stock_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis talks about the price of the stocks mentioned in the premise
if microtron_stock_hypothesis >= microtron_stock_premise:
    # check if the price of MicroTron stock in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif dynaco_stock_hypothesis!= dynaco_stock_premise:
    # check if the price of Dynaco stock in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise:
    # check if the total number of shares sold in the hypothesis contradicts the total number of shares sold reported in the premise
    label = "contradiction"
elif average_price_hypothesis!= average_price_premise:
    # check if the average price of the shares sold in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
