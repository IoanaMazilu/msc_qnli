# Premise: Matt and Peter can do together a piece of work in 20 days.
# Hypothesis: Matt and Peter can do together a piece of work in less than 50 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 50

# the hypothesis talks about the time needed by Matt and Peter to do a piece of work, referenced also in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the time needed by Matt and Peter to do a piece of work, according to the premise
    label = "contradiction"
elif work_days_hypothesis > work_days_premise:
    # check if the hypothesis value is greater than the time needed by Matt and Peter to do a piece of work, according to the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

