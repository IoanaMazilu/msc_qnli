carpet_coverage_premise = 20
carpet_coverage_hypothesis = 40

# the hypothesis refers to the percentage of carpet coverage in Andrea's living room, mentioned in the premise
if carpet_coverage_hypothesis!= carpet_coverage_premise:
    # check if the carpet coverage percentage in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
