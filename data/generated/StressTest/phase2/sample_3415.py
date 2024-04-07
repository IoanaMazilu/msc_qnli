# Premise: less than 50% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Hypothesis: 30% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Golden Label: neutral

death_rate_premise = 50
death_rate_hypothesis = 30
left_rate = 25 # same in both premise and hypothesis

# the hypothesis talks about the death and leaving rate of the people in a village in Sri Lanka, referenced also in the premise
if death_rate_hypothesis >= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the estimate of less than 'death_rate_premise'
    label = "contradiction"
elif left_rate != left_rate:
    # check if the leaving rate in the hypothesis contradicts the leaving rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

