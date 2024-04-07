# Premise: Another survey of 120 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of less than 120 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_surveyed_premise = 120
people_surveyed_hypothesis = 120
preference_rate_premise = 60
preference_rate_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the preference rate mentioned in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the estimate of 'people_surveyed_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preference_rate_hypothesis != preference_rate_premise:
    # check if the preference rate in the hypothesis contradicts the preference rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

