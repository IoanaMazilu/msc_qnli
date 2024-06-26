days_premise = 11
days_hypothesis = 81

# the hypothesis refers to the number of days it takes Mary to complete a piece of work
# the premise mentions a specific number of days, but does not provide an estimate
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of days, but any number of days greater than that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
