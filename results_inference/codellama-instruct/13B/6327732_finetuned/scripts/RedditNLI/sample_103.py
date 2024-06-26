# extract the year from the premise and hypothesis
year_premise = 2008
year_hypothesis = 2006

# check if the year in the hypothesis contradicts the year in the premise
if year_hypothesis < year_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
