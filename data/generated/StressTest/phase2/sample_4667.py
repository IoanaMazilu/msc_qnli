# Premise: Another survey of 150 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 750 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_surveyed_premise = 150
people_surveyed_hypothesis = 750
brand_A_preference_premise = 60
brand_A_preference_hypothesis = 60

# the premise and the hypothesis both refer to a survey of people in the town of Angie and their preference for Brand A
if people_surveyed_premise != people_surveyed_hypothesis:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed mentioned in the premise
    label = "contradiction"
elif brand_A_preference_premise != brand_A_preference_hypothesis:
    # check if the percentage of people who preferred Brand A in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # the premise values and the hypothesis values are consistent with each other, but the premise does not explicitly entail the hypothesis
    label = "neutral"

print(label)

