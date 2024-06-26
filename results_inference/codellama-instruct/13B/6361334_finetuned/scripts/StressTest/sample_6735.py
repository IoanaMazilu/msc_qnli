days_rohit_premise = 12
days_rohit_hypothesis = 22
days_rohan_premise = 6
days_rohan_hypothesis = 6

# the hypothesis refers to the number of days it takes for Rohit and Rohan to complete a work
# the premise mentions the number of days for Rohit and Rohan separately
if days_rohit_hypothesis <= days_rohit_premise:
    # check if the estimate of 'days_rohit_hypothesis' contradicts the number of days for Rohit in the premise
    label = "contradiction"
elif days_rohan_hypothesis!= days_rohan_premise:
    # check if the number of days for Rohan in the hypothesis contradicts the number of days for Rohan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
