interest_premise = 8
interest_hypothesis = 7

# the hypothesis talks about a higher interest rate than the premise
if interest_hypothesis <= interest_premise:
    # check if the hypothesis value contradicts the estimate of the interest rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate higher than 'interest_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
