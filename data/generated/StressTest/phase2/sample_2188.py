# Premise: Another survey of less than 300 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 100 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: neutral

people_surveyed_premise = 300
people_surveyed_hypothesis = 100
brand_A_preference_premise = 60
brand_A_preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the percentage of preference for Brand A mentioned in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the premise estimation of less than 'people_surveyed_premise'
    label = "contradiction"
elif brand_A_preference_hypothesis != brand_A_preference_premise:
    # check if the preference for Brand A in the hypothesis contradicts the preference reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones
    # the premise suggests a number of surveyed people less than 'people_surveyed_premise', thus a number less than that can be inferred
    label = "entailment"

print(label)

