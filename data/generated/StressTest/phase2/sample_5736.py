# Premise: Matt and Peter can do together a piece of work in 20 days.
# Hypothesis: Matt and Peter can do together a piece of work in less than 70 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 70

# the hypothesis refers to the number of days required to complete a piece of work by both Matt and Peter, as mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # check if the 'work_days_hypothesis' is equal to the number of work days in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, we can infer neutrality
    label = "neutral"

print(label)

