# Premise: 15% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Hypothesis: less than 15% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Golden Label: contradiction

percentage_died_premise = 15
percentage_died_hypothesis = 15
percentage_left_premise = 25
percentage_left_hypothesis = 25

# the hypothesis refers to the percentage of people who died and who left the village, as mentioned in the premise
if percentage_died_hypothesis >= percentage_died_premise:
    # check if the percentage of people who died in the hypothesis contradicts the percentage of people who died in the premise
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

