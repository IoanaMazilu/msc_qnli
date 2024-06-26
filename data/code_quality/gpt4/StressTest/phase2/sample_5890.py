distance_behind_premise = 60
distance_behind_hypothesis = 10

# the hypothesis talks about the distance Esha was behind when Banu reached the goal post, referenced also in the premise
if distance_behind_hypothesis > distance_behind_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_behind_premise'
    label = "contradiction"
elif distance_behind_hypothesis < distance_behind_premise:
    # the premise gives only an estimate for the distance Esha was behind
    # any distance less than 'distance_behind_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis is exactly 'distance_behind_premise', we can infer entailment
    label = "entailment"

print(label)
