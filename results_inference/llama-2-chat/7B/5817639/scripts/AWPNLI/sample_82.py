# Define variables for the premise and hypothesis
Premise = {"cards_premise": 33.0, "torn_cards_premise": 6.0, "new_cards_premise": 23.0}
Hypothesis = {"cards_hypothesis": 56.0}

# Compare the variables to determine the label
if Premise["cards_premise"] + Premise["new_cards_premise"] == Hypothesis["cards_hypothesis"]:
    label = "entailment"
elif Hypothesis["cards_hypothesis"] - Premise["cards_premise"] > Premise["torn_cards_premise"]:
    label = "contradiction"
else:
    label = "neutral"

print(label)
