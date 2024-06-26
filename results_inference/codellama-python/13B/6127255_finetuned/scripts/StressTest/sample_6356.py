microtron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis refers to the same situation as the premise, but with different prices per share
if microtron_price_hypothesis!= microtron_price_premise:
    # check if the microtron price in the hypothesis contradicts the microtron price in the premise
    label = "contradiction"
elif dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the dynaco price in the hypothesis contradicts the dynaco price in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise:
    # check if the total number of shares in the hypothesis contradicts the total number of shares in the premise
    label = "contradiction"
elif average_price_hypothesis!= average_price_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
