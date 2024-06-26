run_deficit_premise = 150
run_deficit_hypothesis = 150

# the hypothesis mentions the run deficit, which is also referenced in the premise
if run_deficit_hypothesis!= run_deficit_premise:
    # check if the run deficit in the hypothesis contradicts the run deficit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
