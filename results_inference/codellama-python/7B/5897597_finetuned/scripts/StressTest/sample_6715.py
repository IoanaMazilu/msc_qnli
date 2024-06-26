ferrari_plate_premise = 7
ferrari_plate_hypothesis = 5

# the hypothesis talks about the number of the plate of Sachin's Ferrari, referenced also in the premise
if ferrari_plate_hypothesis >= ferrari_plate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ferrari_plate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of the plate
    # any number of the plate less than 'ferrari_plate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
