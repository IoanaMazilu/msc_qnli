rohit_days_premise = 12
rohan_days_premise = 6
rohit_days_hypothesis = 62
rohan_days_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan need to complete a work, mentioned in the premise
if rohit_days_hypothesis!= rohit_days_premise:
    # check if the number of days Rohit needs in the hypothesis contradicts the number of days Rohit needs in the premise
    label = "contradiction"
elif rohan_days_hypothesis!= rohan_days_premise:
    # check if the number of days Rohan needs in the hypothesis contradicts the number of days Rohan needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
