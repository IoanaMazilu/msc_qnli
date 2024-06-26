years_future_premise = 6
years_future_hypothesis = 3

# the hypothesis talks about the number of years until Arun's age reaches 26, referenced also in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_future_premise' years
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
