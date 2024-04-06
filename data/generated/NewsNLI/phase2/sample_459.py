# Premise: Too Short's manager David Weintraub acknowledged to CNN that Short's breath test at the scene tested'' 0.01 above the limit in California.''
# Hypothesis: Too Short's breath tested'' 0.01 above the limit in California'' for alcohol, manager says.
# Golden Label: entailment

alcohol_level_premise = 0.01
alcohol_level_hypothesis = 0.01

# the hypothesis mentions the alcohol level in Too Short's breath, which is also mentioned in the premise
if alcohol_level_hypothesis != alcohol_level_premise:
    # check if the alcohol level in the hypothesis contradicts the alcohol level reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

