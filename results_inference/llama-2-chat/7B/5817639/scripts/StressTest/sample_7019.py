seniors_premise = 300
seniors_hypothesis = 400

# the hypothesis refers to the number of seniors at Morse High School, which is also mentioned in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors, and the hypothesis value is consistent with it
    label = "neutral"

print(label)
