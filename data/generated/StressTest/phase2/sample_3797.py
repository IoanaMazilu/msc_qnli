# Premise: Another survey of 125 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of more than 125 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_surveyed_premise = 125
people_surveyed_hypothesis = 125
brandA_preference_premise = 60
brandA_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the percentage of preference for Brand A
if brandA_preference_hypothesis != brandA_preference_premise:
    # check if the preference for Brand A in the hypothesis contradicts the preference reported in the premise
    label = "contradiction"
elif people_surveyed_hypothesis <= people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed in the premise
    label = "contradiction"
else:
    # the premise does not provide a maximum limit for the number of people surveyed
    # any number of people surveyed greater than 'people_surveyed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

