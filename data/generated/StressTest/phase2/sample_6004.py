# Premise: John needs more than 3 balls out of 10 balls.
# Hypothesis: John needs 4 balls out of 10 balls.
# Golden Label: neutral

balls_needed_premise = 3
balls_needed_hypothesis = 4
total_balls = 10

# the hypothesis talks about the number of balls John needs, referenced also in the premise
if balls_needed_hypothesis <= balls_needed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'balls_needed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls greater than 'balls_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

