import re

# define variables with representative names for the numerical entities in both inputs
weeks_premise = re.findall(r'\d+', "two-three weeks")[0]
weeks_hypothesis = re.findall(r'\d+', "two to three weeks")[0]

# extract all quantities as valid numbers (integers or floats)
weeks_premise = int(weeks_premise)
weeks_hypothesis = int(weeks_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if weeks_hypothesis!= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
