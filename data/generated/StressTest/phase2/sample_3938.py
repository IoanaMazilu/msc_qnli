# Premise: 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: less than 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 5
death_rate_hypothesis = 5
left_rate_premise = 15
left_rate_hypothesis = 15

# the hypothesis refers to the death and leaving rates of people in a village mentioned in the premise
if death_rate_hypothesis >= death_rate_premise:
    # check if the 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
elif left_rate_hypothesis != left_rate_premise:
    # check if the leaving rate in the hypothesis contradicts the leaving rate reported in the premise
    label = "contradiction"
else:
    # the hypothesis death rate is less than the premise death rate, so it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

