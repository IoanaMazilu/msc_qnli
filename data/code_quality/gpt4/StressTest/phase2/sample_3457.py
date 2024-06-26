carpet_coverage_premise = 10
carpet_coverage_hypothesis = 30
carpet_size_premise = 4 * 9
carpet_size_hypothesis = 4 * 9

# the hypothesis refers to the percentage of carpet coverage and the size of the carpet mentioned in the premise
if carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the 'carpet_coverage_hypothesis' contradicts the premise estimate of more than 'carpet_coverage_premise'
    label = "contradiction"
elif carpet_size_hypothesis != carpet_size_premise:
    # check if the size of the carpet in the hypothesis contradicts the size of the carpet reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of carpet coverage
    # any percentage of carpet coverage greater than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
