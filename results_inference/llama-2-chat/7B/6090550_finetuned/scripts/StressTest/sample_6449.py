john_future_age_premise = 5
john_future_age_hypothesis = 7

# the hypothesis talks about the future age of John, referenced also in the premise
if john_future_age_hypothesis!= john_future_age_premise:
    # check if the future age of John in the hypothesis contradicts the future age of John in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
