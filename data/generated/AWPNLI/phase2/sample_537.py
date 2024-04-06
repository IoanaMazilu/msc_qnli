# Premise: 20.0 ducks are swimming in a lake and 13.0 ducks leave.
# Hypothesis: 11.0 ducks are swimming in the lake.
# Golden Label: contradiction

ducks_start_premise = 20.0
ducks_leave_premise = 13.0
ducks_hypothesis = 11.0

# the hypothesis refers to the number of ducks in the lake, which is also referred to in the premise
# compute the number of ducks left in the lake in the premise
ducks_left_premise = ducks_start_premise - ducks_leave_premise
if ducks_hypothesis != ducks_left_premise:
    # check if the number of ducks in the hypothesis contradicts the number of ducks left in the lake from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

