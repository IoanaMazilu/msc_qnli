# Premise: 10% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: less than 70% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: entailment

death_rate_premise = 10
death_rate_hypothesis = 70
left_rate = 15

# the hypothesis refers to the death and departure rates mentioned in the premise
if death_rate_hypothesis < death_rate_premise:
    # check if the 'death_rate_hypothesis' contradicts the death rate reported in the premise
    label = "contradiction"
elif left_rate != left_rate:
    # check if the departure rate in the hypothesis contradicts the departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

