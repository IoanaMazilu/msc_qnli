# Premise: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: less than 30% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: entailment

percentage_died_premise = 10
percentage_left_premise = 20
percentage_died_hypothesis = 30
percentage_left_hypothesis = 20

# the hypothesis refers to the percentage of people who died and left the village mentioned in the premise
if percentage_died_premise >= percentage_died_hypothesis:
    # check if the estimate of 'percentage_died_hypothesis' contradicts the percentage of people who died in the premise
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

