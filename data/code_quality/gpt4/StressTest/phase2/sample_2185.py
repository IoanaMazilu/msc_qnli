years_future_premise = 3
years_future_hypothesis = 4

# The hypothesis refers to the number of years in the future where John will be twice as old as Frank, also mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the number of years stated in the hypothesis contradicts the estimate of more than 'years_future_premise' years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
