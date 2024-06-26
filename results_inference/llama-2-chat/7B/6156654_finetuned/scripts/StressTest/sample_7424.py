floor_premise = 51
floor_hypothesis = 81
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor and rate Albert gets on the elevator at the same time as the premise
if floor_hypothesis == floor_premise:
    # check if the hypothesis value contradicts the premise value
    if rate_hypothesis!= rate_premise:
        label = "contradiction"
    else:
        label = "entailment"
else:
    # if the hypothesis floor value doesn't match the premise, we can't infer entailment
    label = "contradiction"

print(label)
