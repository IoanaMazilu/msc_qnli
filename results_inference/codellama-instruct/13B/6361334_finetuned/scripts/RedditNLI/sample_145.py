# define variables for the numerical entities in the premise and hypothesis
gdp_premise = 2017
gdp_hypothesis = 2017

# the hypothesis and premise mention the year of the GDP report
if gdp_premise!= gdp_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
