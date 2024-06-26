price_change_premise = -28
price_change_hypothesis = -28
price_increase_next_month = 5

# the hypothesis talks about the price change in the last 3 months and the next one month, which are also mentioned in the premise
if price_change_hypothesis!= price_change_premise:
    # check if the price change in the hypothesis contradicts the price change in the premise
    label = "contradiction"
else:
    # if the price change in the hypothesis does not contradict the price change in the premise, we can infer entailment
    label = "entailment"

print(label)
