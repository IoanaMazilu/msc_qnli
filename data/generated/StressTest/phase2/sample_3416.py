# Premise: 30% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Hypothesis: less than 30% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Golden Label: contradiction

people_died_premise = 30
people_died_hypothesis = 30
people_left_premise = 25
people_left_hypothesis = 25

# the hypothesis refers to the percentage of people who died or left, mentioned in the premise
if people_died_hypothesis >= people_died_premise:
    # check if the estimate of 'people_died_hypothesis' contradicts the percentage of people died in the premise
    label = "contradiction"
elif people_left_hypothesis != people_left_premise:
    # check if the percentage of people left in the hypothesis contradicts the percentage of people who left reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

