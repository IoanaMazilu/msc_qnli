# Premise: Another survey of less than 325 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 125 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: neutral

people_surveyed_premise = 325
people_surveyed_hypothesis = 125
brand_preference_premise = 60
brand_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the brand preference, both referenced in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the premise estimate of less than 'people_surveyed_premise'
    label = "contradiction"
elif brand_preference_hypothesis != brand_preference_premise:
    # check if the brand preference in the hypothesis contradicts the brand preference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

