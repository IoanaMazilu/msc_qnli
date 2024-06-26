# The premise and hypothesis mention the same game and score
if score_premise!= score_hypothesis:
    # Check if the score in the premise contradicts the score in the hypothesis
    label = "contradiction"
else:
    # If the scores match, it is an entailment
    label = "entailment"

print(label)
