carpet_coverage_premise = 20
carpet_coverage_hypothesis = 40

# the hypothesis talks about the percentage of carpet coverage in the living room floor, referenced also in the premise
if carpet_coverage_hypothesis!= carpet_coverage_premise:
    # check if the percentage of carpet coverage in the hypothesis contradicts the percentage of carpet coverage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
