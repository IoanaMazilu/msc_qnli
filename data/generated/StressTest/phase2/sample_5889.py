# Premise: When Banu reached the goal post Esha was 10 m behind.
# Hypothesis: When Banu reached the goal post Esha was less than 60 m behind.
# Golden Label: entailment

distance_behind_premise = 10
distance_behind_hypothesis = 60

# the hypothesis refers to the distance between Banu and Esha at the goal post, which is also mentioned in the premise
if distance_behind_hypothesis < distance_behind_premise:
    # check if the hypothesis value contradicts the exact distance provided in the premise
    label = "contradiction"
elif distance_behind_hypothesis == distance_behind_premise:
    # if the distance in the hypothesis exactly matches the one in the premise, we can infer entailment
    label = "entailment"
else:
    # any distance less than 'distance_behind_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

