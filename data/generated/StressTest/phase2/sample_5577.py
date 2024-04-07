# Premise: 75 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: less than 85 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: entailment

carpet_coverage_premise = 75
carpet_coverage_hypothesis = 85

# the hypothesis refers to the percentage of Andrea's living room floor covered by a carpet
if carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the carpet coverage
    # any percentage less than 'carpet_coverage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

