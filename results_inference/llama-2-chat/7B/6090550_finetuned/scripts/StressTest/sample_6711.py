balls_premise = 17
balls_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike, which is also mentioned in the premise
if balls_premise >= balls_hypothesis:
    # check if the number of balls in the premise contradicts the estimate of less than 'balls_hypothesis'
    label = "contradiction"
elif balls_premise < balls_hypothesis:
    # if the number of balls in the premise is less than 'balls_hypothesis', it is consistent with the hypothesis
    # but we cannot explicitly entail this from the premise, since the exact number is unknown
    label = "neutral"

print(label)
