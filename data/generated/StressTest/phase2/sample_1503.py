# Premise: Cathy runs at 10 miles per hour, and Jim runs at 6 miles per hour.
# Hypothesis: Cathy runs at less than 50 miles per hour, and Jim runs at 6 miles per hour.
# Golden Label: entailment

cathy_speed_premise = 10
jim_speed_premise = 6
cathy_speed_hypothesis = 50
jim_speed_hypothesis = 6

# the hypothesis talks about the speed of Cathy and Jim, referenced also in the premise
if cathy_speed_premise >= cathy_speed_hypothesis:
    # check if the premise value contradicts the estimate of less than 'cathy_speed_hypothesis'
    label = "contradiction"
elif jim_speed_hypothesis != jim_speed_premise:
    # check if the speed of Jim in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives exact values for the speeds of Cathy and Jim
    # the hypothesis does not contradict these values, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

