year_recession_premise = 2009
year_recession_hypothesis = 2009

# the hypothesis and premise mention the year of the last recession in South Africa
if year_recession_hypothesis != year_recession_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)