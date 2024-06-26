chairs_premise = 4
chairs_hypothesis = 6

# the hypothesis talks about the number of chairs needed for seating, referenced also in the premise
if chairs_hypothesis <= chairs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'chairs_premise'
    label = "contradiction"
elif chairs_hypothesis > chairs_premise:
    # the premise gives only an estimate for the number of chairs
    # any number of chairs greater than 'chairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
