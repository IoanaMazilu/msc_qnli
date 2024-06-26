years_premise = 14
years_hypothesis = 14

# the hypothesis refers to a time period in the future, mentioned also in the premise
if years_hypothesis < years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the time period specified in the premise
    label = "contradiction"
else:
    # both sentences are identical, except for the term that estimates the time period
    # any time period equal or greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
