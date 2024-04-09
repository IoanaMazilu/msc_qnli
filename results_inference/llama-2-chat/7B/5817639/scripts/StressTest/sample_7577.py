sreedhar_sravan_premise = 25
sreedhar_sravan_hypothesis = 30

# the hypothesis refers to the number of days it would take Sreedhar and Sravan to complete a work, mentioned in the premise
if sreedhar_sravan_premise <= sreedhar_sravan_hypothesis:
    # check if the estimate of'sreedhar_sravan_hypothesis' contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days, any number of days greater than'sreedhar_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
