seniors_premise = 300
seniors_hypothesis = 600

# the hypothesis refers to the number of seniors at Morse High School, which is also mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the hypothesis value contradicts the number of seniors in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of seniors, but the hypothesis gives an estimate
    # any number of seniors less than'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
