# Premise: 30 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: more than 10 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: entailment

carpet_coverage_premise = 30
carpet_coverage_hypothesis = 10

# the hypothesis refers to the percentage of carpet coverage mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the estimate of 'carpet_coverage_hypothesis' contradicts the carpet coverage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

