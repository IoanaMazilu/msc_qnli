price_crude_premise = 28
price_crude_hypothesis = 28

# the hypothesis refers to the percentage of price decrease in the premise
if price_crude_hypothesis >= price_crude_premise:
    # check if the percentage of price decrease in the hypothesis contradicts the percentage of price decrease reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
