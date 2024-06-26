seniors_morse_premise = 300
seniors_morse_hypothesis = 300
cars_morse_premise = 0.5
cars_morse_hypothesis = 0.5

# the hypothesis talks about the number of seniors in a school, referenced also in the premise
if seniors_morse_hypothesis <= seniors_morse_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_morse_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors greater than'seniors_morse_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
