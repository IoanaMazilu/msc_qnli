seniors_premise = 500
seniors_hypothesis = 300

# the hypothesis talks about the number of seniors at Morse High School, and the premise gives an estimate for the number of seniors and a percentage of them having cars
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of'seniors_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors, and the hypothesis value is consistent with that estimate
    label = "neutral"

print(label)
