# Premise: Altogether, Steve is spending 6 hours a day on the roads.
# Hypothesis: Altogether, Steve is spending less than 7 hours a day on the roads.
# Golden Label: entailment

road_time_premise = 6
road_time_hypothesis = 7

# the hypothesis talks about the number of hours Steve spends on the roads, which is also mentioned in the premise
if road_time_hypothesis <= road_time_premise:
    # check if the estimate of 'road_time_hypothesis' contradicts the time mentioned in the premise
    label = "contradiction"
elif road_time_premise != road_time_hypothesis:
    # check if the time mentioned in the hypothesis contradicts the time reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

