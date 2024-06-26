microtron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis talks about the price and total shares of both stocks, which are also mentioned in the premise
if microtron_price_hypothesis!= microtron_price_premise or dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the prices of either stock in the hypothesis contradict the prices mentioned in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise:
    # check if the total shares sold in the hypothesis contradict the total shares sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
