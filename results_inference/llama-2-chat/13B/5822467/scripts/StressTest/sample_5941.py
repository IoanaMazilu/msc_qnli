# Define variables for numerical entities in the premise and hypothesis
mala_gangs_premise = 2
mala_gangs_hypothesis = 5

# Extract numerical information from the premise and hypothesis
ways_to_invite_premise = mala_gangs_premise * (mala_gangs_premise + 1) / 2
ways_to_invite_hypothesis = mala_gangs_hypothesis * (mala_gangs_hypothesis + 1) / 2

# Compare the variables to determine the label
if ways_to_invite_hypothesis > ways_to_invite_premise:
    # The hypothesis implies more ways to invite gangs than the premise, so the label is entailment
    label = "entailment"
elif ways_to_invite_hypothesis < ways_to_invite_premise:
    # The hypothesis implies fewer ways to invite gangs than the premise, so the label is contradiction
    label = "contradiction"
else:
    # The premise and hypothesis have the same number of ways to invite gangs, so the label is neutral
    label = "neutral"

print(label)
