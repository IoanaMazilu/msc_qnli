james_hours_premise = 61
james_hours_hypothesis = 41

# the hypothesis refers to the number of hours James worked, which is also mentioned in the premise
if james_hours_hypothesis >= james_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of hours James worked in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
