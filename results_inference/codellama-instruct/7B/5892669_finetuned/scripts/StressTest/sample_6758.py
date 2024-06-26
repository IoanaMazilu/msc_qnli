tom_goes_premise = 8
tom_goes_hypothesis = 6

# the hypothesis refers to the time when Tom goes, mentioned in the premise
if tom_goes_hypothesis!= tom_goes_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
