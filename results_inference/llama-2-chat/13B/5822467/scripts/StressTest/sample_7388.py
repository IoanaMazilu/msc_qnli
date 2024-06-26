mary_work_premise = 11
mary_work_hypothesis = 15

# the hypothesis refers to the number of days needed to complete a piece of work
if mary_work_hypothesis > mary_work_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif mary_work_hypothesis == mary_work_premise:
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
