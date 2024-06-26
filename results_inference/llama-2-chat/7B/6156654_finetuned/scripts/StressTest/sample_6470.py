carpet_coverage_premise = 0.2
carpet_coverage_hypothesis = 0.4

# the hypothesis refers to the percentage of the floor covered by the carpet, which is also mentioned in the premise
if carpet_coverage_hypothesis!= carpet_coverage_premise:
    # check if the percentage of the floor covered by the carpet in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentages are the same, it's an entailment
    label = "entailment"

print(label)
