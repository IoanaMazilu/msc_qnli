years_future_premise = 88
years_future_hypothesis = 18

# the hypothesis refers to Molly's future age, which is also mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the number of future years in the hypothesis contradicts the premise estimate of less than 'years_future_premise'
    label = "contradiction"
elif years_future_hypothesis < years_future_premise:
    # the premise gives only an estimate for the number of future years
    # any number of future years less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
