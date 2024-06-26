profit_premise = 6970
profit_hypothesis = 1970

# the hypothesis talks about the profit, which is also mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the profit value in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
