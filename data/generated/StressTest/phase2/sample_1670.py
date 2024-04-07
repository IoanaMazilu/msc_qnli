# Premise: 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: more than 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 5
death_rate_hypothesis = 5
flee_rate_premise = 15
flee_rate_hypothesis = 15

# the hypothesis talks about the percentage of people who died and who fled from a village in Sri Lanka, referenced also in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'death_rate_premise' 
    label = "contradiction"
elif flee_rate_premise != flee_rate_hypothesis:
    # check if the number of people who fled in the hypothesis contradicts the number of people who fled reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of people who died
    # any percentage of death rate greater than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

