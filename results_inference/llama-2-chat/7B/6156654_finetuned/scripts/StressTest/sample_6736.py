rohit_work_days_premise = 22
rohan_work_days_premise = 6
work_days_hypothesis = 12
rohit_work_days_hypothesis = 6

# the hypothesis refers to the number of days required by Rohit and Rohan to complete a work, as stated in the premise
if rohit_work_days_hypothesis!= rohit_work_days_premise:
    # check if the number of days Rohit needs to complete the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif rohan_work_days_hypothesis!= rohan_work_days_premise:
    # check if the number of days Rohan needs to complete the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
