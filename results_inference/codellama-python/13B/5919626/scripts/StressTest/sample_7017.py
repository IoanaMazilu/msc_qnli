seniors_premise = 300
seniors_hypothesis = 800
cars_premise = 40
cars_hypothesis = 40

# the hypothesis talks about the number of seniors in a school, referenced also in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors greater than'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
