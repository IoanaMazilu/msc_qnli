homes_repossessed_premise = 1000000
homes_repossessed_hypothesis = 1000000
year_premise = 2010
year_hypothesis = 2010

# the hypothesis and premise mention the number of homes repossessed and the year
if homes_repossessed_hypothesis != homes_repossessed_premise or year_hypothesis != year_premise:
    # check if the number of homes repossessed and the year in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
