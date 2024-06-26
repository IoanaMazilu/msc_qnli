pat_stretch_premise = 20
cara_run_premise = 20
pat_stretch_hypothesis = 80
cara_run_hypothesis = 20

# the hypothesis talks about the time Pat needs to stretch and the time Cara runs
if pat_stretch_hypothesis <= pat_stretch_premise:
    # check if the hypothesis value contradicts the estimate of Pat's stretching time in the premise
    label = "contradiction"
elif cara_run_hypothesis!= cara_run_premise:
    # check if the number of minutes Cara runs in the hypothesis contradicts the number of minutes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
