micro_tron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

micro_tron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis refers to the price and number of shares of the same stocks mentioned in the premise
if micro_tron_price_hypothesis!= micro_tron_price_premise or dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the prices of the stocks in the hypothesis contradict the prices reported in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise or average_price_hypothesis!= average_price_premise:
    # check if the number of shares or average price in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
