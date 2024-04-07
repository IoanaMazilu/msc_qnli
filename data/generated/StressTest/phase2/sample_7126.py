# Premise: How many miles from home can Aaron jog so that he spends a total of more than 1 hours jogging and walking?
# Hypothesis: How many miles from home can Aaron jog so that he spends a total of 3 hours jogging and walking?
# Golden Label: neutral

hours_jogging_walking_premise = 1
hours_jogging_walking_hypothesis = 3

# the hypothesis is about the total hours Aaron can spend jogging and walking, which is also mentioned in the premise
if hours_jogging_walking_hypothesis <= hours_jogging_walking_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_jogging_walking_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total hours 
    # any number of hours greater than 'hours_jogging_walking_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

