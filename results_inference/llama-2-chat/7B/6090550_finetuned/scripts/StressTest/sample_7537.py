somenumber_premise = [50, 60, 70, 80, 80]
somenumber_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis talks about the scores obtained by Reeya in different subjects, which is also mentioned in the premise
if somenumber_hypothesis <= somenumber_premise:
    # check if the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
