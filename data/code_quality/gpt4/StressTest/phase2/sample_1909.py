hours_watched_tv_premise = 5
hours_watched_tv_hypothesis_lower = 1
hours_watched_tv_hypothesis_upper = 2

# the hypothesis refers to the number of hours Pat watched TV last week, also mentioned in the premise
if hours_watched_tv_hypothesis_lower >= hours_watched_tv_premise:
    # check if the lower estimate of 'hours_watched_tv_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
elif hours_watched_tv_hypothesis_upper > hours_watched_tv_premise:
    # check if the upper estimate of 'hours_watched_tv_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
