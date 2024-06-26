less_than_premise = 536
hypothesis_watermelons = 136

# the hypothesis talks about the number of watermelons after Sally left
if hypothesis_watermelons <= less_than_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons after Sally left
    # any number of watermelons greater than 'less_than_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
