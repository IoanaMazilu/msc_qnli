# Premise: Mike gives you another less than 77 balls.
# Hypothesis: Mike gives you another 17 balls.
# Golden Label: neutral

balls_given_premise = 77
balls_given_hypothesis = 17

# the hypothesis refers to the number of balls given by Mike, also mentioned in the premise
if balls_given_hypothesis >= balls_given_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_given_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of balls
    # any number less than 'balls_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

