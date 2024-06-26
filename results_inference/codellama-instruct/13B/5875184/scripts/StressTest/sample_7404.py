lenses_premise = 2
lenses_hypothesis = 7
tubes_premise = 1
tubes_hypothesis = 1
eyepieces_premise = 1
eyepieces_hypothesis = 1

# the hypothesis talks about the number of lenses in a telescope
if lenses_hypothesis <= lenses_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lenses_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of lenses
    # any number of lenses greater than 'lenses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
