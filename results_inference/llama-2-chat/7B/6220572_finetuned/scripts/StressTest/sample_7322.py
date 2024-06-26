gym_visits_premise = 3
gym_visits_hypothesis = 1

# the hypothesis talks about the number of gym visits in a week, referenced also in the premise
if gym_visits_hypothesis == gym_visits_premise:
    # check if the hypothesis value contradicts the number of gym visits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gym visits
    # any number of gym visits consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
