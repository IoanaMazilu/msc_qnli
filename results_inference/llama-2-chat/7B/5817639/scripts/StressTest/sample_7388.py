mary_work_premise = 11
mary_work_hypothesis = float("+inf")

# the hypothesis refers to the number of days Mary can do a piece of work, while the premise gives an estimate
if mary_work_premise <= mary_work_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than'mary_work_premise' days
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days, so any number greater than'mary_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
