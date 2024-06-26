number_premise = 4
number_hypothesis = 8

# the hypothesis refers to the same number as in the premise, but with a different bound
if number_hypothesis <= number_premise:
    # check if the hypothesis bound contradicts the premise
    label = "contradiction"
elif number_hypothesis > number_premise:
    # check if the premise number contradicts the hypothesis number
    label = "contradiction"
else:
    # if the hypothesis number is less than or equal to the premise number, it does not contradict it
    # and we can infer entailment
    label = "entailment"

print(label)
