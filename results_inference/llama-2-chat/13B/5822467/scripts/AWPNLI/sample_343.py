father_gathered_premise = 20.0
senior_ranger_gathered_premise = 20.0
total_wood_gathered_premise = father_gathered_premise + senior_ranger_gathered_premise
sacks_filled_hypothesis = 6.0
total_wood_gathered_hypothesis = 80.0

# compare the total amount of wood gathered in the premise and hypothesis
if total_wood_gathered_hypothesis > total_wood_gathered_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif total_wood_gathered_hypothesis < total_wood_gathered_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise have the same value, so there is no contradiction or entailment
    label = "neutral"

print(label)
