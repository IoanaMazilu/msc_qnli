lists_premise = 4/4
lists_hypothesis = 1/4

# the hypothesis refers to the number of top-10 movie lists a film must appear in to be considered for movie of the year
if lists_hypothesis >= lists_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif lists_hypothesis < lists_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is consistent with the premise and can be explicitly entailed
    label = "entailment"

print(label)
