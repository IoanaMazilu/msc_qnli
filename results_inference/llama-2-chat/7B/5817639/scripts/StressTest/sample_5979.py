seniors_premise = 300
seniors_hypothesis = 600

# the hypothesis talks about the number of seniors at Morse High School, which is different from the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of'seniors_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of seniors, and the hypothesis value is greater than that estimate
    # therefore, the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
