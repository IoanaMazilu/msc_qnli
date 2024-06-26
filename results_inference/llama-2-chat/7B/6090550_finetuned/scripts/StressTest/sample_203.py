y_premise = 5
y_hypothesis = 5

# the hypothesis refers to the number of days they worked together, which is also mentioned in the premise
if y_hypothesis!= y_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

