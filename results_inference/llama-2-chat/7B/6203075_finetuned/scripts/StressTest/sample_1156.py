year_premise = 2979
year_hypothesis = 1979

# the hypothesis refers to the same year as the premise, but with a different number of passengers
if year_hypothesis == year_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    if 1/3 * 37.3e6!= 1/3 * 37.3e6:
        label = "contradiction"
    else:
        label = "entailment"
else:
    # if the hypothesis year is not the same as the premise year, the hypothesis cannot be entailed
    label = "neutral"

print(label)
