year_premise = 2006
year_hypothesis = 2008

# the hypothesis and premise mention the year when the interest rate was raised in Hong Kong and Mexico respectively
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
