# Define the possible scores that Mary got in the game according to the premise and hypothesis
possible_scores_premise = [1, 2, 3]
possible_scores_hypothesis = [less than 1, 2, 3]

# The hypothesis refers to the scores that Mary got in the game, which are also mentioned in the premise
if possible_scores_hypothesis[0] >= possible_scores_premise[0]:
    # Check if the first possible score in the hypothesis contradicts the first possible score in the premise
    label = "contradiction"
elif possible_scores_hypothesis[1]!= possible_scores_premise[1] or possible_scores_hypothesis[2]!= possible_scores_premise[2]:
    # Check if the second or third possible score in the hypothesis contradicts the second or third possible score in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
