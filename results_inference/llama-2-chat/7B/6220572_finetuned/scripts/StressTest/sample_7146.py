square_premise = 0
square_hypothesis = 8

# the hypothesis talks about the number of squares mentioned in the premise
if square_hypothesis <= square_premise:
    # check if the hypothesis value contradicts the estimate of less than'square_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of squares
    # any number of squares less than'square_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
