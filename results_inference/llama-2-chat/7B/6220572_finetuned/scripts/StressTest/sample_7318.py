minutes_jim_premise = 78
minutes_jim_hypothesis = 18

# the hypothesis refers to the number of minutes Jim takes to stretch, mentioned also in the premise
if minutes_jim_hypothesis >= minutes_jim_premise:
    # check if the estimate of'minutes_jim_hypothesis' contradicts the number of minutes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of minutes Jim takes to stretch
    # any number of minutes less than'minutes_jim_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
