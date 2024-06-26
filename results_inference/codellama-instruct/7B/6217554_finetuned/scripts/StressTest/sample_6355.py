microtron_stock_premise = 76
microtron_stock_hypothesis = 36
dynaco_stock_premise = 48
dynaco_stock_hypothesis = 48
shares_sold_premise = 300
shares_sold_hypothesis = 300
average_price_per_share_premise = 40
average_price_per_share_hypothesis = 40

# the hypothesis talks about the price of the stocks and the number of shares sold, referenced also in the premise
if microtron_stock_hypothesis >= microtron_stock_premise:
    # check if the price of MicroTron stock in the hypothesis contradicts the estimate of less than'microtron_stock_premise'
    label = "contradiction"
elif dynaco_stock_hypothesis!= dynaco_stock_premise:
    # check if the price of Dynaco stock in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif shares_sold_hypothesis!= shares_sold_premise:
    # check if the number of shares sold in the hypothesis contradicts the number of shares sold reported in the premise
    label = "contradiction"
elif average_price_per_share_hypothesis!= average_price_per_share_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
