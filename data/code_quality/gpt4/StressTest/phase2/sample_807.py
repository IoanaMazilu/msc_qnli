years_ago_premise = 5
years_ago_hypothesis = 7

# the hypothesis refers to a timing in the past that is also mentioned in the premise
if years_ago_premise > years_ago_hypothesis:
    # check if the premise time contradicts the hypothesis time
    label = "contradiction"
else:
    # the premise gives only a specific time
    # any time less than or equal to 'years_ago_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
