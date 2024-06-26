rohit_days_premise = 12
rohan_days_premise = 6
rohit_days_hypothesis = 22
rohan_days_hypothesis = 6

# the hypothesis gives an estimate for the number of days Rohit and Rohan can complete a work
if rohit_days_hypothesis <= rohit_days_premise:
    # check if the estimate of 'rohit_days_hypothesis' contradicts the number of days Rohit can complete a work in the premise
    label = "contradiction"
elif rohan_days_hypothesis!= rohan_days_premise:
    # check if the number of days Rohan can complete a work in the hypothesis contradicts the number of days Rohan can complete a work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
