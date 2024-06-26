price_change_premise = 68
price_change_hypothesis = 28

# the hypothesis talks about the percentage change in the price of crude oil, which is also mentioned in the premise
if price_change_hypothesis!= price_change_premise:
    # check if the percentage change in the hypothesis contradicts the percentage change in the premise
    label = "contradiction"
else:
    # if the percentage change in the hypothesis does not contradict the percentage change in the premise, we can infer entailment
    label = "entailment"

print(label)
