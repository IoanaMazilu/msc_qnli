# Premise: more than 30 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: 50 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: neutral

carpet_coverage_premise = 30
carpet_coverage_hypothesis = 50

# the hypothesis refers to the carpet coverage of Andrea's living room mentioned in the premise
if carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the carpet coverage percentage in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the carpet coverage
    # any percentage greater than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

