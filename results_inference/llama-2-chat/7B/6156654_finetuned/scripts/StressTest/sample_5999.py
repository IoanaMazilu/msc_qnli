# The hypothesis refers to the same condition as the premise
if hypothesis['appearance_in_lists'] >= premise['appearance_in_lists']:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis doesn't contradict the premise, we can infer entailment
    label = "entailment"

print(label)
