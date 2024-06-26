anita_leaves_premise = 7
anita_leaves_hypothesis = 1
indu_leaves_premise = 7
indu_leaves_hypothesis = 1

# the hypothesis refers to the number of days before the work is finished, also mentioned in the premise
if anita_leaves_hypothesis <= anita_leaves_premise:
    # check if the estimate of 'anita_leaves_hypothesis' contradicts the number of days before Anita leaves in the premise
    label = "contradiction"
elif indu_leaves_hypothesis!= indu_leaves_premise:
    # check if the number of days before Indu leaves in the hypothesis contradicts the number of days before Indu leaves reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
