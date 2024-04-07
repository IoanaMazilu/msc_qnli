# Premise: If, five years from now, the sum E of their ages will be less than 71, how old is Stephanie?
# Hypothesis: If, five years from now, the sum E of their ages will be 51, how old is Stephanie?
# Golden Label: neutral

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

