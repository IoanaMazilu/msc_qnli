year_premise = 2008
year_hypothesis = 2006

# the hypothesis and premise mention the year when the rate was raised
if year_premise != year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis does not contradict the year in the premise, we can infer entailment
    label = "entailment"

print(label)
