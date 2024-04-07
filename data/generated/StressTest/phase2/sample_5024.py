# Premise: The average time of Izzy's past 3 100-meter sprints is 15 seconds.
# Hypothesis: The average time of Izzy's past 6 100-meter sprints is 15 seconds.
# Golden Label: contradiction

avg_time_sprints_premise = 15
sprint_count_premise = 3
avg_time_sprints_hypothesis = 15
sprint_count_hypothesis = 6

# the hypothesis talks about the average time of Izzy's sprints and the number of sprints, the same as the premise
if avg_time_sprints_hypothesis != avg_time_sprints_premise:
    # check if the average time of sprints in the hypothesis contradicts the average time of sprints reported in the premise
    label = "contradiction"
elif sprint_count_hypothesis != sprint_count_premise:
    # check if the number of sprints in the hypothesis contradicts the number of sprints reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

