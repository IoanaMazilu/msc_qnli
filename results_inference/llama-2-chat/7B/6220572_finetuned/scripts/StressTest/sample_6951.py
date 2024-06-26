years_future_premise = 5
years_future_hypothesis = 2

# the hypothesis refers to the number of years until Arun's age reaches 40, which is also mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_future_premise' years until Arun's age reaches 40
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years until Arun's age reaches 40
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
