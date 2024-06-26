# extract the year from the premise and hypothesis
year_premise = 2017
year_hypothesis = 2017

# the hypothesis and premise mention the year
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same year
    # any mention of the year in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
