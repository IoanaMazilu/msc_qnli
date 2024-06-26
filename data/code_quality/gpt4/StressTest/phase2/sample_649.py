innings_premise = 86
innings_hypothesis = 16

# the hypothesis talks about the number of innings Suraj has played, referenced also in the premise
if innings_hypothesis >= innings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'innings_premise'
    label = "contradiction"
elif innings_hypothesis < innings_premise:
    # the premise gives only an estimate for the number of innings
    # any number of innings less than 'innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)
