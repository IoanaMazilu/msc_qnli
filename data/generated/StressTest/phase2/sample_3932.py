# Premise: 60 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: more than 60 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: contradiction

carpet_coverage_percentage_premise = 60
carpet_coverage_percentage_hypothesis = 60

# the hypothesis refers to the percentage of the floor covered by a carpet mentioned in the premise
if carpet_coverage_percentage_hypothesis <= carpet_coverage_percentage_premise:
    # check if the hypothesis value contradicts the exact percentage of floor coverage in the premise
    label = "contradiction"
else:
    # the premise gives an exact percentage for the carpet coverage
    # any percentage greater than 'carpet_coverage_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

