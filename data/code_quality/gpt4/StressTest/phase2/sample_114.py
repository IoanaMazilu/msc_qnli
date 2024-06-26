clean_time_premise = 3
clean_time_hypothesis = 6

# the hypothesis refers to the time to clean the house if Anne's speed were doubled
if clean_time_hypothesis < clean_time_premise:
    # check if the hypothesis value contradicts the premise's cleaning time
    label = "contradiction"
elif clean_time_hypothesis > clean_time_premise:
    # check if the hypothesis value is more than the premise's cleaning time
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise's cleaning time, we can infer entailment
    label = "entailment"

print(label)
