rohit_work_days_premise = 12
rohan_work_days_premise = 6
rohit_work_days_hypothesis = 22
rohan_work_days_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan need to complete a work, mentioned in the premise
if rohit_work_days_hypothesis <= rohit_work_days_premise:
    # check if the estimate of 'rohit_work_days_hypothesis' contradicts the number of days Rohit needs in the premise
    label = "contradiction"
elif rohan_work_days_hypothesis!= rohan_work_days_premise:
    # check if the number of days Rohan needs in the hypothesis contradicts the number of days Rohan needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
