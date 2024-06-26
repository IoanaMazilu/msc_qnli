people_surveyed_premise = 120
people_surveyed_hypothesis = 520
brand_preference_premise = 60
brand_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the brand preference mentioned in the premise
if people_surveyed_premise >= people_surveyed_hypothesis:
    # check if the estimate of 'people_surveyed_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif brand_preference_hypothesis!= brand_preference_premise:
    # check if the brand preference in the hypothesis contradicts the brand preference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
