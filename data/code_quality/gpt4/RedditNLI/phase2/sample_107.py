min_decision_time_premise = 2
max_decision_time_premise = 3
min_decision_time_hypothesis = 2
max_decision_time_hypothesis = 3

# the hypothesis and premise mention the time frame in which Trump will decide on the new Fed chair
if min_decision_time_hypothesis < min_decision_time_premise or max_decision_time_hypothesis > max_decision_time_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
