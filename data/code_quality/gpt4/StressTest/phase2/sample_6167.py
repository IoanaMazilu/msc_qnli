money_premise = 95
money_hypothesis = 95

# the hypothesis refers to the amount of money mentioned in the premise
if money_hypothesis < money_premise:
    # check if the hypothesis value contradicts the exact amount 'money_premise'
    label = "contradiction"
elif money_hypothesis > money_premise:
    # check if the hypothesis value contradicts the exact amount 'money_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
