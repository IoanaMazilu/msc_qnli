year_premise = 2006
year_hypothesis = 2008

# the hypothesis and premise mention the year when a base rate was raised, which is also mentioned in the sentences
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
