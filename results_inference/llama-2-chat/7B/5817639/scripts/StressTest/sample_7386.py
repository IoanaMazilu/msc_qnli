mary_work_premise = 11
mary_work_hypothesis = 81

# the hypothesis refers to a faster completion time of a piece of work than the premise
if mary_work_hypothesis <= mary_work_premise:
    # check if the hypothesis value contradicts the estimate of less than'mary_work_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Mary to complete a piece of work, while the hypothesis gives a faster estimate
    # any faster completion time than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
