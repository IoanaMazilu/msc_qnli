sreedhar_sravan_premise = 35
sreedhar_sravan_hypothesis = 25

# the hypothesis talks about the time it takes for Sreedhar and Sravan to do a work, referenced also in the premise
if sreedhar_sravan_hypothesis <= sreedhar_sravan_premise:
    # check if the hypothesis value contradicts the estimate of less than'sreedhar_sravan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes for Sreedhar and Sravan to do a work
    # any time less than'sreedhar_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
