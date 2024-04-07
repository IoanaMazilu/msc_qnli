# Premise: The average time of Izzy's past less than 7 100-meter sprints is 15 seconds.
# Hypothesis: The average time of Izzy's past 3 100-meter sprints is 15 seconds.
# Golden Label: neutral

sprints_premise = 7
sprints_hypothesis = 3
average_time_premise = 15
average_time_hypothesis = 15

# the hypothesis refers to the number of Izzy's sprints and their average time, which are also mentioned in the premise
if sprints_hypothesis >= sprints_premise:
    # check if the number of sprints in the hypothesis contradicts the estimate of less than 'sprints_premise' in the premise
    label = "contradiction"
elif average_time_hypothesis != average_time_premise:
    # check if the average time in the hypothesis contradicts the average time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

