people_surveyed_premise = 130
people_surveyed_hypothesis = 630
preference_premise = 60
preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed in the town of Angie and their brand preference, both mentioned in the premise
if people_surveyed_hypothesis < people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preference_hypothesis != preference_premise:
    # check if the brand preference percentage in the hypothesis contradicts the brand preference percentage reported in the premise
    label = "contradiction"
elif people_surveyed_hypothesis == people_surveyed_premise and preference_hypothesis == preference_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a specific number of people surveyed and their preference
    # any number of people surveyed less than 'people_surveyed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
