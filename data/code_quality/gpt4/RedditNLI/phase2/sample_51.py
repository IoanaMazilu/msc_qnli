year_premise = 2016
year_hypothesis = 2016

# the hypothesis and premise mention the year when middle-class incomes reached the highest-ever level
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis does not contradict the year in the premise, we can infer entailment
    label = "entailment"

print(label)
