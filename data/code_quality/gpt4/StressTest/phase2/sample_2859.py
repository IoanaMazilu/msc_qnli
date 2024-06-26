max_score_premise = 5
max_score_hypothesis = 6

# the hypothesis talks about the maximum score in a game, referenced also in the premise
if max_score_hypothesis <= max_score_premise:
    # check if the hypothesis value contradicts the premise information
    label = "contradiction"
elif max_score_hypothesis > max_score_premise:
    # check if the hypothesis value is not entailed by the premise information
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
