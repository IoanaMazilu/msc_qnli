# Premise: Another survey of 100 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 700 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_surveyed_premise = 100
people_surveyed_hypothesis = 700
preference_premise = 60
preference_hypothesis = 60

# the hypothesis refers to the people surveyed and brand preference in the premise
if people_surveyed_premise != people_surveyed_hypothesis:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preference_premise != preference_hypothesis:
    # check if the brand preference percentage in the hypothesis contradicts the brand preference percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, there is no explicit entailment here
    label = "neutral"

print(label)

