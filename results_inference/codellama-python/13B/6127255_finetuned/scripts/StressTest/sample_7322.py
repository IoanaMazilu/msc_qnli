#week_premise = 3
#week_hypothesis = 1
#gym_visit_premise = 2
#gym_visit_hypothesis = 2

# the hypothesis refers to the number of weeks and gym visits mentioned in the premise
# if the number of weeks in the hypothesis is more than the number of weeks in the premise, it contradicts the premise
if week_hypothesis > week_premise:
    label = "contradiction"
# if the number of weeks in the hypothesis is equal to the number of weeks in the premise, it doesn't contradict the premise
elif week_hypothesis == week_premise:
    # if the number of gym visits in the hypothesis is equal to the number of gym visits in the premise, it doesn't contradict the premise
    if gym_visit_hypothesis == gym_visit_premise:
        label = "entailment"
    # if the number of gym visits in the hypothesis is more than the number of gym visits in the premise, it contradicts the premise
    elif gym_visit_hypothesis > gym_visit_premise:
        label = "contradiction"
    # if the number of gym visits in the hypothesis is less than the number of gym visits in the premise, it doesn't contradict the premise
    elif gym_visit_hypothesis < gym_visit_premise:
        label = "neutral"
# if the number of weeks in the hypothesis is less than the number of weeks in the premise, it doesn't contradict the premise
elif week_hypothesis < week_premise:
    label = "neutral"

print(label)
