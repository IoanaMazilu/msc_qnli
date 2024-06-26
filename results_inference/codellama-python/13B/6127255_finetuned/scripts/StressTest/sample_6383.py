hours_regular_premise = 40
hours_regular_hypothesis = 50

# the hypothesis refers to the hours of regular work mentioned in the premise
if hours_regular_hypothesis!= hours_regular_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
