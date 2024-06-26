ime_jogging_premise = 3
time_jogging_walking_premise = 3

time_jogging_walking_hypothesis = 4

# the hypothesis refers to the time Aaron spends jogging and walking from home, which is also mentioned in the premise
if time_jogging_walking_hypothesis!= time_jogging_walking_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
