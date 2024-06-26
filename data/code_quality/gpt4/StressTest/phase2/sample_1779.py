years_back_premise = 6
years_back_hypothesis = 2

# the hypothesis refers to the same context as the premise, but the years back are different
if years_back_hypothesis >= years_back_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific point of time (6 years back)
    # any point of time less than 6 years back is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
