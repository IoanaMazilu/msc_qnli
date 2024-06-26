goal_premise = 3
goal_hypothesis = 3

# the hypothesis mentions the score of West Ham in the second half, which is not explicitly mentioned in the premise
# however, the premise does mention that West Ham recovered from being 3-0 down at halftime
if goal_hypothesis == goal_premise:
    # the hypothesis and premise both mention the same score, so there is no contradiction or entailment
    label = "neutral"
else:
    # if the hypothesis mentions a different score than the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
