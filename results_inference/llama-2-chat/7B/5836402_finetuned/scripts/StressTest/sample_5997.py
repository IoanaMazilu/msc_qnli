lists_premise = 10
lists_hypothesis = 4/4

# the hypothesis refers to the number of movie lists that a film must appear in to be considered for'movie of the year', mentioned in the premise
if lists_hypothesis >= lists_premise:
    # check if the hypothesis value contradicts the premise value of at least 1/4 of the top-10-movies lists
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
