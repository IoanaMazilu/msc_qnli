# Premise: Jaydeep purchased 25 kg of rice at the rate of 16.50 per kg and 35 kg of rice at the rate of 24.50 per kg.
# Hypothesis: Jaydeep purchased less than 75 kg of rice at the rate of 16.50 per kg and 35 kg of rice at the rate of 24.50 per kg.
# Golden Label: entailment

rice_kg_premise1 = 25
rate_premise1 = 16.50
rice_kg_premise2 = 35
rate_premise2 = 24.50

rice_kg_hypothesis1 = 75
rate_hypothesis1 = 16.50
rice_kg_hypothesis2 = 35
rate_hypothesis2 = 24.50

# the hypothesis talks about the amount of rice and the price per kg mentioned in the premise
if rice_kg_premise1 >= rice_kg_hypothesis1:
    # check if the amount of rice in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif rate_hypothesis1 != rate_premise1:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif rice_kg_hypothesis2 != rice_kg_premise2:
    # check if the amount of rice in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif rate_hypothesis2 != rate_premise2:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

