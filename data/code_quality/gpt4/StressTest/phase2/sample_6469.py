carpet_coverage_premise = 30
carpet_coverage_hypothesis = 20

# the hypothesis talks about the carpet coverage of Andrea's living room floor, referenced also in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carpet_coverage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the carpet coverage
    # any percentage less than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
