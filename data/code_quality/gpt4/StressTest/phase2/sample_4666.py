people_surveyed_premise = 250
people_surveyed_hypothesis = 150
brand_A_preference_premise = 60
brand_A_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and their preference for Brand A, which is also mentioned in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the estimate of less than 'people_surveyed_premise'
    label = "contradiction"
elif brand_A_preference_hypothesis != brand_A_preference_premise:
    # check if the preference for Brand A in the hypothesis contradicts the preference for Brand A reported in the premise
    label = "contradiction"
else:
    # any number of people surveyed less than 'people_surveyed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
