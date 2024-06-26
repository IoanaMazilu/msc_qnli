people_surveyed_premise = 150
people_surveyed_hypothesis = 250
percentage_brandA_premise = 60
percentage_brandA_hypothesis = 60

# the hypothesis refers to the number of surveyed people and the preference for Brand A in the premise
if people_surveyed_hypothesis <= people_surveyed_premise:
    # check if the hypothesis value contradicts the number of people surveyed in the premise
    label = "contradiction"
elif percentage_brandA_hypothesis != percentage_brandA_premise:
    # check if the percentage of people preferring Brand A in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
