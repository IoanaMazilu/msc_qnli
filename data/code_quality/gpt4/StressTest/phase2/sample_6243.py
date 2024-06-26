people_surveyed_premise = 120
people_surveyed_hypothesis = 520
brand_a_preference_premise = 60
brand_a_preference_hypothesis = 60

# the hypothesis talks about the number of people surveyed and the preference percentage for Brand A, both referenced in the premise
if people_surveyed_hypothesis <= people_surveyed_premise:
    # check if the hypothesis estimate contradicts the number of people surveyed in the premise
    label = "contradiction"
elif brand_a_preference_hypothesis != brand_a_preference_premise:
    # check if the preference percentage for Brand A in the hypothesis contradicts the preference percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
