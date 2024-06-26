microtron_stock_premise = 56
microtron_stock_hypothesis = 36
dynaco_stock_premise = 60
dynaco_stock_hypothesis = 60
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis talks about the price of MicroTron and Dynaco stock per share, total shares sold and average price per share mentioned in the premise
if microtron_stock_hypothesis >= microtron_stock_premise:
    # check if the price of MicroTron stock per share in the hypothesis contradicts the price in the premise
    label = "contradiction"
elif dynaco_stock_hypothesis != dynaco_stock_premise:
    # check if the price of Dynaco stock per share in the hypothesis contradicts the price in the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise:
    # check if the total shares sold in the hypothesis contradicts the total shares sold in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
