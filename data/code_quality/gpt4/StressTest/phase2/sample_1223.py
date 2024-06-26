carpet_coverage_premise = 50
carpet_coverage_hypothesis = 50
carpet_size_premise = (4, 9)
carpet_size_hypothesis = (4, 9)

# the hypothesis refers to the carpet coverage and size mentioned in the premise
if carpet_coverage_hypothesis <= carpet_coverage_premise:
    # check if the estimate of 'carpet_coverage_hypothesis' contradicts the carpet coverage in the premise
    label = "contradiction"
elif carpet_size_hypothesis != carpet_size_premise:
    # check if the carpet size in the hypothesis contradicts the carpet size reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact carpet coverage and size
    # any carpet coverage more than 'carpet_coverage_premise' with the same size is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
