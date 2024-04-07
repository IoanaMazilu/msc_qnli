# Premise: John gives you another 100 balls.
# Hypothesis: John gives you another less than 100 balls.
# Golden Label: contradiction

balls_given_premise = 100
balls_given_hypothesis = 100

# the hypothesis talks about the number of balls given by John, mentioned in the premise
if balls_given_hypothesis >= balls_given_premise:
    # check if the hypothesis value contradicts the premise statement of 'another 100 balls'
    label = "contradiction"
else:
    # the premise gives an exact number of balls given
    # any number less than 'balls_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

