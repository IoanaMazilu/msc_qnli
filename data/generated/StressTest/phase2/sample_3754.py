# Premise: Another survey of less than 630 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 130 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: neutral

people_surveyed_premise = 630
people_surveyed_hypothesis = 130
brand_preference_premise = 60
brand_preference_hypothesis = 60

# the hypothesis talks about the number of people surveyed in the town of Angie, the same as the premise
# it also mentions the brand preference, which is the same in both the premise and the hypothesis
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the number of people surveyed in the hypothesis contradicts the premise estimate of less than 'people_surveyed_premise'
    label = "contradiction"
elif brand_preference_hypothesis != brand_preference_premise:
    # check if the brand preference in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, they are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

