john_gives_balls_premise = 100
john_gives_balls_hypothesis = 300

# the hypothesis refers to the number of balls given by John
if john_gives_balls_hypothesis < john_gives_balls_premise:
    # the hypothesis value is less than the premise value, so there is no contradiction
    label = "neutral"
else:
    # the hypothesis value is greater than or equal to the premise value, so we can compare the estimates
    if john_gives_balls_hypothesis > john_gives_balls_premise:
        # the hypothesis value is greater than the premise value, so we can infer entailment
        label = "entailment"
    else:
        # the hypothesis value is less than or equal to the premise value, so we cannot infer entailment or contradiction
        label = "neutral"

print(label)
