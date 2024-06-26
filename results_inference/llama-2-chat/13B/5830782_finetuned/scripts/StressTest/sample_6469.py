carpet_coverage_premise = 30
carpet_coverage_hypothesis = 20

# the hypothesis refers to the percentage of carpet coverage in Andrea's living room mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the estimate of 'carpet_coverage_hypothesis' contradicts the maximum percentage of carpet coverage in the premise
    label = "contradiction"
elif carpet_coverage_hypothesis < carpet_coverage_premise:
    # the premise gives only an estimate for the maximum percentage of carpet coverage
    # any percentage of carpet coverage less than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
