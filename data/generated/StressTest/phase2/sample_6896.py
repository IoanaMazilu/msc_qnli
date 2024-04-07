# Premise: Alice walked for 3 days.
# Hypothesis: Alice walked for 6 days.
# Golden Label: contradiction

walking_days_premise = 3
walking_days_hypothesis = 6

# the hypothesis talks about the number of days Alice walked, referenced also in the premise
if walking_days_hypothesis == walking_days_premise:
    # check if the number of walking days in the hypothesis is the same as in the premise
    label = "entailment"
elif walking_days_hypothesis < walking_days_premise:
    # check if the number of walking days in the hypothesis contradicts the number of walking days reported in the premise
    label = "contradiction"
else:
    # the number of walking days in the hypothesis is more than the one reported in the premise
    # this does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

