number_premise = 7
number_hypothesis = 3

# the hypothesis refers to the same number as the premise, but with a different base
if number_premise!= number_hypothesis:
    # check if the number in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
