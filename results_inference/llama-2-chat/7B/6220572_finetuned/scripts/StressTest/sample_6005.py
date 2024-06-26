balls_premise = 10
balls_hypothesis = 10

# the hypothesis talks about the number of balls John needs, also referenced in the premise
if balls_hypothesis == balls_premise:
    # check if the number of balls in the hypothesis contradicts the number of balls reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
