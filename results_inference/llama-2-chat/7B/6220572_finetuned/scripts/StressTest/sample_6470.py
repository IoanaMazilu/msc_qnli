carpet_coverage_premise = 20
carpet_coverage_hypothesis = 40
carpet_dimensions_premise = (4, 9)
carpet_dimensions_hypothesis = (4, 9)

if carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the percentage of the floor covered by the carpet in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the floor covered by the carpet
    # any percentage greater than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
