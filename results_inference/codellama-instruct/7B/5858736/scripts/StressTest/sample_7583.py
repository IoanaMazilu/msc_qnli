sravan_premise = 0
sreedhar_premise = 75
sravan_hypothesis = 0
sreedhar_hypothesis = 0

# the hypothesis refers to the number of days required to complete the work
if sreedhar_premise <= sreedhar_hypothesis:
    # check if the estimate of'sreedhar_hypothesis' contradicts the number of days required to complete the work in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days required to complete the work
    # any number of days greater than'sreedhar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
