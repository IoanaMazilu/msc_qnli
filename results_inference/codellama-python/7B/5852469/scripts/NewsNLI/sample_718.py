amount_raised_premise = 350000
amount_raised_hypothesis = 350000

# the hypothesis mentions the amount of money raised by the foundation, which is also mentioned in the premise
if amount_raised_hypothesis!= amount_raised_premise:
    # check if the amount raised from the hypothesis contradicts the amount raised in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
