year_premise = 2005

# the hypothesis and premise mention the year of the Bankruptcy Reform
if year_premise!= 2005:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
