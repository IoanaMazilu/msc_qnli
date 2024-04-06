# Premise: The key message -- keep baby monitors at least 3 feet away from cribs.
# Hypothesis: The key piece of advice is to keep monitors at least 3 feet away from cribs.
# Golden Label: entailment

distance_premise = 3
distance_hypothesis = 3

# the hypothesis mentions the same distance for keeping monitors away from cribs as the premise
if distance_premise != distance_hypothesis:
    # check if the recommended distance in the hypothesis contradicts the recommended distance in the premise
    label = "contradiction"
else:
    # if the recommended distance from the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
