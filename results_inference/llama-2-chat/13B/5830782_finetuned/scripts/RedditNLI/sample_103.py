year_premise = 2008
year_hypothesis = 2006

# the hypothesis and premise mention the year when a rate was raised for the first time since then
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
