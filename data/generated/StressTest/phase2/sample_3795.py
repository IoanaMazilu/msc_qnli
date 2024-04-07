# Premise: Another survey of 125 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of less than 325 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: entailment

people_surveyed_premise = 125
people_surveyed_hypothesis = 325
brand_a_preference_premise = 60
brand_a_preference_hypothesis = 60

# the hypothesis refers to the people surveyed and preference for Brand A mentioned in the premise
if people_surveyed_hypothesis <= people_surveyed_premise:
    # check if the estimate of 'people_surveyed_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif brand_a_preference_hypothesis != brand_a_preference_premise:
    # check if the preference for Brand A in the hypothesis contradicts the preference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

