balls_given = 77
balls_hypothesis = 17

# the hypothesis talks about the number of balls Mike gives you, which is also mentioned in the premise
if balls_hypothesis >= balls_given:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif balls_hypothesis < balls_given:
    # the hypothesis value is less than the premise value, so it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it can be explicitly entailed from the premise
    label = "entailment"

print(label)
