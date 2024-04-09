carpet_coverage_premise = 30
carpet_coverage_hypothesis = 20

# the hypothesis refers to the carpet coverage mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carpet_coverage_premise'
    label = "contradiction"
elif carpet_coverage_hypothesis < carpet_coverage_premise:
    # the premise gives only an estimate for the carpet coverage
    # any percentage less than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
