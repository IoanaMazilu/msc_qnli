dist_premise = 800
dist_hypothesis = 100

# the hypothesis talks about the distance between Fred and Sam, which is also referred to in the premise
if dist_hypothesis <= dist_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dist_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Fred and Sam
    # any distance greater than 'dist_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
