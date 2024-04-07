# Premise: for Mathura and B starts from Mathura with a speed of less than 65 kmph at 8 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of 25 kmph at 8 p.
# Golden Label: neutral

speed_B_premise = 65
speed_B_hypothesis = 25

# the hypothesis specifies the speed of B when starting from Mathura, which is also mentioned in the premise
if speed_B_hypothesis >= speed_B_premise:
    # check if the hypothesis speed contradicts the premise's estimation of less than 'speed_B_premise'
    label = "contradiction"
elif speed_B_hypothesis < speed_B_premise:
    # if the speed in the hypothesis is less than 'speed_B_premise', it is consistent with the premise
    # since the premise does not define an exact speed, but gives only an upper limit, we can't infer entailment
    label = "neutral"
    
print(label)

