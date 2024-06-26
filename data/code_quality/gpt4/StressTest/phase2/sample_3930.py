carpet_coverage_premise = 60
carpet_coverage_hypothesis = 70
carpet_size_premise = (4, 9)
carpet_size_hypothesis = (4, 9)

# the hypothesis talks about the percentage of the living room floor covered by a carpet, and the carpet size, both mentioned in the premise
if carpet_size_premise != carpet_size_hypothesis:
    # check if the carpet size in the hypothesis contradicts the carpet size mentioned in the premise
    label = "contradiction"
elif carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the estimate of 'carpet_coverage_hypothesis' contradicts the carpet coverage percentage in the premise
    label = "contradiction"
else:
    # the premise gives a specific percentage for the carpet coverage
    # any percentage less than 'carpet_coverage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
