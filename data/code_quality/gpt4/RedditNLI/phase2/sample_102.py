year_premise = 2006
year_hypothesis = 2006

# the hypothesis and premise mention the year of the rate hike
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # the hypothesis refers to a rate hike in Hong Kong, which cannot be explicitly entailed from the premise referring to a rate hike by the FED
    label = "neutral"

print(label)
