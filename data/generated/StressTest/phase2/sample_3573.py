# Premise: 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: less than 7% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: entailment

died_premise = 5
died_hypothesis = 7
left_premise = 15
left_hypothesis = 15

# the hypothesis refers to the percentage of people who died and left the village, as mentioned in the premise
if died_hypothesis <= died_premise:
    # check if the 'died_hypothesis' contradicts the percentage of people who died in the premise
    label = "contradiction"
elif left_hypothesis != left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

