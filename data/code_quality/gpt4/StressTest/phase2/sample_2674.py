sum_ages_future_premise = 71
sum_ages_future_hypothesis = 51

# the hypothesis talks about a future combined age, referenced also in the premise
if sum_ages_future_hypothesis >= sum_ages_future_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sum_ages_future_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the future combined age
    # any combined age less than 'sum_ages_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
