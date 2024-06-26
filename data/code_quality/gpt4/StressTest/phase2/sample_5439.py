barrels_produced_premise = 195
barrels_produced_hypothesis = 495

# the hypothesis refers to the number of barrels produced by Little Texas Drilling Company 
if barrels_produced_hypothesis < barrels_produced_premise:
    # check if the estimate of 'barrels_produced_hypothesis' contradicts the number of barrels produced in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of barrels produced, while the hypothesis gives an upper limit
    # thus, the premise does not contradict the hypothesis, but also does not fully entail it
    label = "neutral"

print(label)
