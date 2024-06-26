year_premise = 2017
year_hypothesis = 2017

# the hypothesis and premise mention the year of the slow start of the US economy
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
