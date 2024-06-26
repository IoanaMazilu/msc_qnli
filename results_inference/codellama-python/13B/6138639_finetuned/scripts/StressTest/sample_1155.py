year_premise = 1979
year_hypothesis = 2979

# the hypothesis refers to the same year mentioned in the premise
if year_hypothesis <= year_premise:
    # check if the hypothesis year contradicts the premise year
    label = "contradiction"
else:
    # the premise gives only an estimate for the year
    # any year greater than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
