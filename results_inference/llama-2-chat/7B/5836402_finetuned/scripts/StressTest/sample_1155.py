year_premise = 1979
year_hypothesis = 2979

# the hypothesis refers to the year when the airport was used, which is also mentioned in the premise
if year_hypothesis <= year_premise:
    # check if the hypothesis value contradicts the estimate of more than 'year_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the year
    # any year greater than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
