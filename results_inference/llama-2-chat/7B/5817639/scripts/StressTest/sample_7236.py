miles_premise = 240
miles_hypothesis = 440

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation
if miles_hypothesis <= miles_premise:
    # check if the estimate of'miles_hypothesis' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance traveled, but the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
