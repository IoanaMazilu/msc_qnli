microtron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis refers to the price per share of MicroTron and Dynaco stocks, as well as the total shares sold, which are also mentioned in the premise
if microtron_price_hypothesis!= microtron_price_premise or dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the prices per share in the hypothesis contradict the prices per share mentioned in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise or average_price_hypothesis!= average_price_premise:
    # check if the total shares sold or the average price per share in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
