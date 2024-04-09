raise_average_premise = 7
raise_average_hypothesis = 2

# the hypothesis talks about raising the average score, referenced also in the premise
if raise_average_hypothesis >= raise_average_premise:
    # check if the hypothesis value contradicts the estimate of less than 'raise_average_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the raise in average score
    # any raise less than 'raise_average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
