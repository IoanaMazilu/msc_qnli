money_premise = 248
money_hypothesis = 148

# the hypothesis refers to the amount of money Marie has in her bank account, mentioned in the premise
if money_hypothesis!= money_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
