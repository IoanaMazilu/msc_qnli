tom_goes_after_premise = 8
tom_goes_after_hypothesis = 6

if tom_goes_after_hypothesis!= tom_goes_after_premise:
    # check if the number of P in the hypothesis contradicts the number of P reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
