ana_time_premise = 2
ana_time_hypothesis = 8

# the hypothesis talks about the time Ana goes, referenced also in the premise
if ana_time_hypothesis <= ana_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ana_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Ana goes
    # any time greater than 'ana_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
