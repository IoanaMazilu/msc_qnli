miles_traveled_premise = 440
miles_traveled_hypothesis = 240

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation, referenced also in the premise
if miles_traveled_hypothesis >= miles_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than'miles_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance less than'miles_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
