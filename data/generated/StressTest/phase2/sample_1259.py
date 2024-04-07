# Premise: Altogether, Steve is spending 6 hours a day on the roads.
# Hypothesis: Altogether, Steve is spending 7 hours a day on the roads.
# Golden Label: contradiction

road_time_premise = 6
road_time_hypothesis = 7

# the hypothesis talks about the time Steve spends on the roads, which is also mentioned in the premise
if road_time_hypothesis != road_time_premise:
    # check if the time spent on the roads in the hypothesis contradicts the time spent on the roads reported in the premise
    label = "contradiction"
else:
    # if the time spent on the roads in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

