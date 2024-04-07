# Premise: Sakshi can do a piece of work in 20 days.
# Hypothesis: Sakshi can do a piece of work in more than 20 days.
# Golden Label: contradiction

work_days_premise = 20
work_days_hypothesis = 20

# the hypothesis is about the number of days Sakshi needs to do a piece of work, which is also referenced in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_days_premise'
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # the hypothesis value is equal to the premise value, which contradicts the idea of 'more than 20 days'
    label = "contradiction"
else:
    # the premise provides an exact number of days, 'work_days_premise'
    # a hypothesis stating Sakshi needs more days than 'work_days_premise' to do the work does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

