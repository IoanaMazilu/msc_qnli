carpet_coverage_premise = 20
carpet_coverage_hypothesis = 40

# the hypothesis talks about the carpet coverage of Andrea's living room, referenced also in the premise
if carpet_coverage_hypothesis!= carpet_coverage_premise:
    # check if the carpet coverage percentage in the hypothesis contradicts the carpet coverage percentage reported in the premise
    label = "contradiction"
else:
    # if the carpet coverage percentage in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
