# Premise: 20 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: less than 30 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: entailment

carpet_coverage_premise = 20
carpet_coverage_hypothesis = 30

# the hypothesis refers to the percentage of the floor covered by the carpet mentioned in the premise
if carpet_coverage_premise >= carpet_coverage_hypothesis:
    # check if the estimate of 'carpet_coverage_hypothesis' contradicts the percentage of carpet coverage in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

