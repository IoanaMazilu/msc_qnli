years_ago_premise = 5
years_ago_hypothesis = 5

# the hypothesis talks about the same scenario as the premise, but the time reference is different
if years_ago_hypothesis > years_ago_premise:
    # check if the time reference in the hypothesis contradicts the time reference in the premise
    label = "contradiction"
else:
    # if the time reference in the hypothesis does not contradict the time reference in the premise, we can infer entailment
    label = "entailment"

print(label)
