y_premise = 3
y_hypothesis = 4

# the hypothesis refers to the number of fastest horses to be submitted from London Racetrack to Kentucky Derby
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the number of fastest horses in the premise
    label = "contradiction"
elif y_hypothesis > y_premise:
    # check if the hypothesis value is greater than the number of fastest horses in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the number of fastest horses in the premise, we can infer entailment
    label = "entailment"

print(label)
