years_back_premise = 5
years_back_hypothesis = 6

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_back_hypothesis <= years_back_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the time frame
    # any time frame greater than 'years_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
