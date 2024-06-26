total_rent_premise = 160
total_rent_hypothesis = 760

# the hypothesis refers to the total rent of the tool mentioned in the premise
if total_rent_hypothesis!= total_rent_premise:
    # check if the total rent in the hypothesis contradicts the total rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
