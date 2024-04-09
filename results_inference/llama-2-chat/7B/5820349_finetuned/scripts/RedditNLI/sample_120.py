year_rate_raised_premise = 2006
year_rate_raised_hypothesis = 2008

# the hypothesis and premise mention the year when the base rate was raised for the first time
if year_rate_raised_premise!= year_rate_raised_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
