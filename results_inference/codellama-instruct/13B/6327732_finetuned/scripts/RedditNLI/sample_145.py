# define variables for the numerical entities in the premise and hypothesis
gdp_premise = 2017
gdp_hypothesis = 2017

# check if the GDP values in the hypothesis contradict the GDP value in the premise
if gdp_hypothesis!= gdp_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
