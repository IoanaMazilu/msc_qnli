mary_work_premise = 11
mary_work_hypothesis = 81

# the hypothesis refers to the time taken by Mary to complete a piece of work
if mary_work_hypothesis <= mary_work_premise:
    # check if the hypothesis value contradicts the estimate of Mary's time taken in the premise
    label = "contradiction"
elif mary_work_hypothesis > mary_work_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for Mary's time taken
    # any time taken less than'mary_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
