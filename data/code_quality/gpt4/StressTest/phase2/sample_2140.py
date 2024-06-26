speed_premise = 80
speed_hypothesis = 40

# the hypothesis refers to the speed of Bob mentioned in the premise
if speed_hypothesis >= speed_premise:
    # if the speed in the hypothesis contradicts the premise (less than 'speed_premise')
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # the speed in the hypothesis is less than the speed in the premise
    # but we can't be sure that the speed is exactly as in the hypothesis, so we can't infer entailment
    label = "neutral"

print(label)
