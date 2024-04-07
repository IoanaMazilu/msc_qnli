# Premise: 30 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: more than 30 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: contradiction

carpet_coverage_premise = 30
carpet_coverage_hypothesis = 30

# the hypothesis refers to the carpet coverage mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the 'carpet_coverage_hypothesis' contradicts the carpet coverage in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it is neutral
    label = "neutral"

print(label)

