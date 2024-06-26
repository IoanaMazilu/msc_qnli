lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 8

# the hypothesis refers to the number of lenses in a telescope, which is also mentioned in the premise
if lenses_per_telescope_hypothesis <= lenses_per_telescope_premise:
    # check if the estimate of 'lenses_per_telescope_hypothesis' contradicts the number of lenses in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of lenses in a telescope
    # any number of lenses greater than 'lenses_per_telescope_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
