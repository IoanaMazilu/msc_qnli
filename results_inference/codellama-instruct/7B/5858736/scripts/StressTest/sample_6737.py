rohit_days_premise = 12
rohan_days_premise = 6
rohit_days_hypothesis = 62
rohan_days_hypothesis = 6

# the hypothesis talks about the number of days it takes for Rohit and Rohan to complete a work
if rohit_days_hypothesis <= rohit_days_premise:
    # check if the estimate of 'rohit_days_hypothesis' contradicts the number of days it takes for Rohit to complete a work in the premise
    label = "contradiction"
elif rohan_days_hypothesis!= rohan_days_premise:
    # check if the number of days it takes for Rohan to complete a work in the hypothesis contradicts the number of days it takes for Rohan to complete a work in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
