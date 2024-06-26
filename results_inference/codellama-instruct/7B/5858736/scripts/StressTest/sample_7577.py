sreedhar_sravan_premise = 25
sreedhar_sravan_hypothesis = 25

# the hypothesis talks about the number of days it takes for Sreedhar and Sravan to do a work
if sreedhar_sravan_hypothesis <= sreedhar_sravan_premise:
    # check if the hypothesis value contradicts the estimate of'sreedhar_sravan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days it takes for Sreedhar and Sravan to do a work
    # any number of days greater than'sreedhar_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
