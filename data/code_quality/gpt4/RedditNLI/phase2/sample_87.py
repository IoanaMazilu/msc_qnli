year_premise = 2009
year_hypothesis = 2009

# the hypothesis and premise mention the same year when South Africa slides into recession
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
