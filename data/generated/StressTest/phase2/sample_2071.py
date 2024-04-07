# Premise: less than 70% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: 10% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: neutral

percentage_dead_premise = 70
percentage_dead_hypothesis = 10
percentage_left_premise = 15
percentage_left_hypothesis = 15

# The hypothesis talks about the percentage of people who died and left the village, as referenced in the premise
if percentage_dead_hypothesis >= percentage_dead_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'percentage_dead_premise'
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # Check if the hypothesis value contradicts the 'percentage_left_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

