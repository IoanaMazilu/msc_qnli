cindy_thought_premise = 4
cindy_thought_hypothesis = 7
square_pos_int_premise = cindy_thought_premise ** 2
square_pos_int_hypothesis = cindy_thought_hypothesis ** 2

# the hypothesis refers to the difference between the square of a positive integer and Cindy's thought
if square_pos_int_hypothesis - square_pos_int_premise > 0:
    # the hypothesis value is greater than the premise value, entailment is possible
    label = "entailment"
elif square_pos_int_hypothesis - square_pos_int_premise == 0:
    # the hypothesis value is equal to the premise value, neutral
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, contradiction
    label = "contradiction"

print(label)
