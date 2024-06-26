participants_premise = 7
participants_hypothesis = 2

# the hypothesis refers to the number of participants in a cycling race mentioned in the premise
if participants_hypothesis!= participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants reported in the premise
    label = "contradiction"
else:
    # if the number of participants in the hypothesis does not contradict the number of participants in the premise, we can infer entailment
    label = "entailment"

print(label)
