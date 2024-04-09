seniors_premise = 300
seniors_hypothesis = 500

# the hypothesis talks about the number of seniors at Morse High School, which is different from the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of'seniors_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of seniors, and the hypothesis provides a different value
    # any number of seniors greater than'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
