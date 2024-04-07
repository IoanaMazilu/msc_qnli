# Premise: Ajay bought 15 kg of dal at the rate of Rs 14.50 per kg and 10 kg at the rate of Rs 13 per kg.
# Hypothesis: Ajay bought less than 35 kg of dal at the rate of Rs 14.50 per kg and 10 kg at the rate of Rs 13 per kg.
# Golden Label: entailment

dal_kg_premise = 15
dal_rate_premise = 14.50
dal_kg_hypothesis = 35
dal_rate_hypothesis = 14.50
dal_kg2_premise = 10
dal_rate2_premise = 13
dal_kg2_hypothesis = 10
dal_rate2_hypothesis = 13

# the hypothesis refers to the weight and rate of dal bought, both mentioned in the premise
if dal_kg_hypothesis <= dal_kg_premise or dal_rate_hypothesis != dal_rate_premise:
    # check if the weight of dal in the hypothesis contradicts the weight in the premise, or if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif dal_kg2_hypothesis != dal_kg2_premise or dal_rate2_hypothesis != dal_rate2_premise:
    # check if the weight of the second type of dal in the hypothesis contradicts the weight in the premise, or if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif dal_kg_hypothesis > dal_kg_premise and dal_rate_hypothesis == dal_rate_premise and dal_kg2_hypothesis == dal_kg2_premise and dal_rate2_hypothesis == dal_rate2_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

