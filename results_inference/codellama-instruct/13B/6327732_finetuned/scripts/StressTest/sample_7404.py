lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 7

# the hypothesis talks about the number of lenses in a telescope, referenced also in the premise
if lenses_per_telescope_hypothesis <= lenses_per_telescope_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lenses_per_telescope_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of lenses
    # any number of lenses greater than 'lenses_per_telescope_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
