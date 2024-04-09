stops_premise = 10
stops_hypothesis = 20

# the hypothesis talks about the time Pat stops stretching, referenced also in the premise
if stops_hypothesis <= stops_premise:
    # check if the hypothesis value contradicts the estimate of less than'stops_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Pat stops stretching
    # any time less than'stops_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
