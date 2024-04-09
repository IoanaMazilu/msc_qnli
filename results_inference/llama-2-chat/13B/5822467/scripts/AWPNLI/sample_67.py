lyssa_picked_limes_premise = 25.0
mike_picked_limes_premise = 32.0
tom_picked_plums_premise = 12.0

total_limes_premise = lyssa_picked_limes_premise + mike_picked_limes_premise + tom_picked_plums_premise

hypothesis_limes = 61.0

# compare the total number of limes in the premise and the hypothesis
if hypothesis_limes > total_limes_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif hypothesis_limes < total_limes_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
