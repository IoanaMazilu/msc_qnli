year_premise = 2008
year_hypothesis = 2006

# the hypothesis and premise mention the year of the last time the key rate was raised
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
