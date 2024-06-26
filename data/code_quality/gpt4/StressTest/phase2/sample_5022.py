sprints_premise = 3
sprints_hypothesis = 7
avg_time_premise = 15
avg_time_hypothesis = 15

# the hypothesis refers to the average time and number of Izzy's 100-meter sprints mentioned in the premise
if avg_time_premise != avg_time_hypothesis:
    # check if the average time in the hypothesis contradicts the average time reported in the premise
    label = "contradiction"
elif sprints_hypothesis <= sprints_premise:
    # check if the number of sprints in the hypothesis contradicts the number of sprints reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
