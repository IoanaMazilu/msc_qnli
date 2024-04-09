# Define variables for the premise and hypothesis
premise_words = len(Premise.split(" "))
hypothesis_words = len(Hypothesis.split(" "))

# Check if the number of words in the hypothesis contradicts the premise
if hypothesis_words!= premise_words:
    label = "contradiction"
else:
    # Check if the hypothesis contains more words than the premise
    if hypothesis_words > premise_words:
        label = "entailment"
    # If the hypothesis contains fewer words than the premise, it is neutral
    else:
        label = "neutral"

print(label)
