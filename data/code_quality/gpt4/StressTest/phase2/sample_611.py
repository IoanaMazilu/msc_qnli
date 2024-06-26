total_pens_premise = 12
total_pens_hypothesis = 82

# the hypothesis refers to the total number of pens purchased mentioned in the premise
if total_pens_premise != total_pens_hypothesis:
    # check if the total number of pens in the hypothesis contradicts the number of total pens reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
