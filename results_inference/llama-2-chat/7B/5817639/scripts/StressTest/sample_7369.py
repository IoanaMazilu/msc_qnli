average_premise = 15
average_hypothesis = 55

# the hypothesis talks about the average of Suresh's marks in English and History, referenced also in the premise
if average_hypothesis >= average_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average, any value greater than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
