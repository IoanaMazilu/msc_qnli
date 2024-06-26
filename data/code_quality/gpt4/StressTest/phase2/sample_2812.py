# defining scores from the premise and hypothesis
scores_premise = [81, 57, 61, 80, 88]
scores_hypothesis = [71, 57, 61, 80, 88]

# check if scores in hypothesis contradict the premise
for i in range(len(scores_premise)):
    if scores_hypothesis[i] >= scores_premise[i]:
        label = "contradiction"
        break
else:
    # if the scores in the hypothesis do not contradict the premise, then the relation is neutral
    label = "neutral"

print(label)
