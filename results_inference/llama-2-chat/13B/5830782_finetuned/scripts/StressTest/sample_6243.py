people_surveyed_premise = 120
people_surveyed_hypothesis = 520
brandA_preference_premise = 60
brandA_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the preference for Brand A mentioned in the premise
if people_surveyed_premise >= people_surveyed_hypothesis:
    # check if the estimate of 'people_surveyed_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif brandA_preference_hypothesis!= brandA_preference_premise:
    # check if the preference for Brand A in the hypothesis contradicts the preference for Brand A reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)