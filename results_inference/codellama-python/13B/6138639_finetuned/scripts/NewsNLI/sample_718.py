money_raised_premise = 350000
money_raised_hypothesis = 350000

# the hypothesis mentions the amount of money raised by the Jordan Thomas Foundation, which is also mentioned in the premise
if money_raised_hypothesis!= money_raised_premise:
    # check if the amount of money raised in the hypothesis contradicts the amount of money raised in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
