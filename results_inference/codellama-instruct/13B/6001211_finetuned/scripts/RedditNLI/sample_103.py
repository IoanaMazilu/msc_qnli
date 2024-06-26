year_premise = 2008
year_hypothesis = 2006

# the hypothesis and premise mention the year of the rate hike
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # the countries are different, so the rate hike cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
