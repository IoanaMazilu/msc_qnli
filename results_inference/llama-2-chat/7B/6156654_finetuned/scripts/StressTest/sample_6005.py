balls_john_needs_premise = 4
balls_john_needs_hypothesis = 3

# the hypothesis refers to the number of balls John needs, which is also mentioned in the premise
if balls_john_needs_hypothesis!= balls_john_needs_premise:
    # check if the number of balls John needs in the hypothesis contradicts the number of balls John needs in the premise
    label = "contradiction"
else:
    # if the number of balls John needs in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
