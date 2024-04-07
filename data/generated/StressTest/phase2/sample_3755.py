# Premise: Another survey of 130 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of more than 130 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_surveyed_premise = 130
people_surveyed_hypothesis = 130
preference_rate_premise = 60
preference_rate_hypothesis = 60

# the hypothesis talks about the number of people surveyed and the preference rate, both referenced in the premise
if people_surveyed_hypothesis > people_surveyed_premise:
    # check if the hypothesis value contradicts the exact number of 'people_surveyed_premise'
    label = "contradiction"
elif preference_rate_hypothesis != preference_rate_premise:
    # check if the preference rate in the hypothesis contradicts the preference rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

