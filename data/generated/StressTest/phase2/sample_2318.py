# Premise: If in 14 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Hypothesis: If in less than 14 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Golden Label: contradiction

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

