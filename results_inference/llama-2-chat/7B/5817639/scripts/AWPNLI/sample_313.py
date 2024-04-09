pencils_drawer_premise = 43.0
pencils_desk_premise = 19.0
pencils_hypothesis = 81.0

# compare the total number of pencils in the hypothesis with the total number of pencils in the premise
if pencils_hypothesis >= pencils_drawer_premise + pencils_desk_premise:
    # check if the total number of pencils in the hypothesis contradicts the estimate of pencils in the premise
    label = "contradiction"
elif pencils_hypothesis!= pencils_drawer_premise + pencils_desk_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
