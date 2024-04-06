# Premise: South Africa Unexpectedly Slides Into Recession For The First Time Since 2009.
# Hypothesis: South Africas Economy Slips Into First Recession Since 2009.
# Golden Label: entailment

year_premise = 2009
year_hypothesis = 2009

# the hypothesis and premise mention the year the recession last happened
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

