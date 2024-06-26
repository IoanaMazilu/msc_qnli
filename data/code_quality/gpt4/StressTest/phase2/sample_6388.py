balls_premise = 300
balls_hypothesis = 100

# the hypothesis talks about the number of balls John gives you, referenced also in the premise
if balls_hypothesis >= balls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
elif balls_hypothesis < balls_premise:
    # the premise gives only an estimate for the number of balls
    # any number of balls less than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
