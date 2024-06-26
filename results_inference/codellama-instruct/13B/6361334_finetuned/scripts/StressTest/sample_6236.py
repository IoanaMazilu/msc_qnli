speed_premise = 2
speed_hypothesis = 1
time_premise = 3
time_hypothesis = 1.5

# the hypothesis refers to the time it would take to clean the house if Anne's speed were doubled
# the premise mentions the time it would take if Anne's speed were doubled and working at their respective rates
if speed_hypothesis!= speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_hypothesis >= time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
