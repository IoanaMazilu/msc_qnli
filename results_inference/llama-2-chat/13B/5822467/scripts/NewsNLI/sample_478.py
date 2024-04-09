abdulmolah_premise = "Opposition spokesman Shamsiddin Abdulmolah told CNN that rebels flew two attack helicopters from Tobruk to join the fighting in Ajdabiya."
helicopters_hypothesis = "Two opposition helicopters attack in Ajdabiya."

# extract numerical entities from the premise and hypothesis
num_entities_premise = ["two attack helicopters"]
num_entities_hypothesis = ["two opposition helicopters"]

# compare the numerical entities in the premise and hypothesis
if len(num_entities_premise) > 0 and len(num_entities_hypothesis) > 0:
    # check if the number of helicopters in the hypothesis contradicts the number of helicopters in the premise
    if len(num_entities_hypothesis)!= len(num_entities_premise):
        label = "contradiction"
    elif num_entities_hypothesis[0]!= num_entities_premise[0]:
        label = "contradiction"
    else:
        # if the number of helicopters in the hypothesis and premise are the same, we can infer entailment
        label = "entailment"
else:
    # if there are no numerical entities in the premise or hypothesis, the relation is neutral
    label = "neutral"

print(label)
