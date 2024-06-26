microtron_price_premise = 36
microtron_price_hypothesis = 36
dynaco_price_premise = 44
dynaco_price_hypothesis = 44
shares_total_premise = 300
shares_total_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the same prices, total number of shares and average price per share as in the premise
if microtron_price_hypothesis <= microtron_price_premise:
    # check if the hypothesis value for MicroTron per share price contradicts the premise
    label = "contradiction"
elif dynaco_price_hypothesis != dynaco_price_premise or shares_total_hypothesis != shares_total_premise or average_price_hypothesis != average_price_premise:
    # check if the hypothesis values for Dynaco per share price, total number of shares or average price per share contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
