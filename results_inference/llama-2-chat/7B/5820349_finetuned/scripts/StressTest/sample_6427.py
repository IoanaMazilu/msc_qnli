value_premise = 750
value_hypothesis = 450

# the hypothesis talks about the value of something sold to George, referenced also in the premise
if value_hypothesis >= value_premise:
    # check if the hypothesis value contradicts the estimate of less than 'value_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value
    # any value less than 'value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
