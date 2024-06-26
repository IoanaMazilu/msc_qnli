concession_premise = 80
concession_hypothesis = 30

# the hypothesis talks about the concession percentage Tarun got, which is also referenced in the premise
if concession_hypothesis >= concession_premise:
    # check if the hypothesis value contradicts the estimate of less than 'concession_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the concession percentage
    # any concession percentage less than 'concession_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
