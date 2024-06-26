less_than_750_premise = 750
sold_to_george_hypothesis = 450

# the hypothesis talks about the amount of money sold to George, referenced also in the premise
if sold_to_george_hypothesis <= less_than_750_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_750_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money sold,
    # any amount of money sold greater than 'less_than_750_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
