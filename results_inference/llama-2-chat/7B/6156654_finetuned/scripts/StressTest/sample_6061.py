anita_leaves_premise = 1
indu_leaves_premise = 1
work_finished_days = 7

# the hypothesis talks about Anita and Indu leaving, which is also mentioned in the premise
if anita_leaves_premise!= indu_leaves_premise:
    # check if the number of days Anita and Indu leave is different in the premise and the hypothesis
    label = "contradiction"
elif work_finished_days!= 7:
    # check if the number of days the work will be finished is different in the premise and the hypothesis
    label = "contradiction"
else:
    # if the number of days Anita and Indu leave and the number of days the work will be finished are the same in both premise and hypothesis, we can infer entailment
    label = "entailment"

print(label)
