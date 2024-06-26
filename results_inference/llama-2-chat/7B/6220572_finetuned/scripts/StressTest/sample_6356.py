microtron_share_price_premise = 36
microtron_share_price_hypothesis = 76
dynaco_share_price_premise = 48
dynaco_share_price_hypothesis = 48
shares_sold_premise = 300
shares_sold_hypothesis = 300
average_price_per_share_premise = 40
average_price_per_share_hypothesis = 40

# the hypothesis refers to the price per share and the number of shares sold of MicroTron and Dynaco stocks, as well as the average price per share
if microtron_share_price_hypothesis!= microtron_share_price_premise or \
   dynaco_share_price_hypothesis!= dynaco_share_price_premise or \
   shares_sold_hypothesis!= shares_sold_premise or \
   average_price_per_share_hypothesis!= average_price_per_share_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
