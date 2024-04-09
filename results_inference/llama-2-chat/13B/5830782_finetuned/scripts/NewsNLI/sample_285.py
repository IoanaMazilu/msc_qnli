winning_margin_premise = 15
winning_margin_hypothesis = 15

# the hypothesis mentions the winning margin for each Spurs victory, which is also mentioned in the premise
if winning_margin_hypothesis!= winning_margin_premise:
    # check if the winning margin in the hypothesis contradicts the winning margin reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
