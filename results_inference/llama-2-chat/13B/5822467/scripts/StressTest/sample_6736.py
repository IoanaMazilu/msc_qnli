rohit_days_premise = 22
rohit_days_hypothesis = 12
rohan_days_premise = 6
rohan_days_hypothesis = 6

# the hypothesis refers to the number of days taken by Rohit and Rohan to complete the work
if rohit_days_premise <= rohit_days_hypothesis and rohan_days_premise <= rohan_days_hypothesis:
    # check if the estimates of both Rohit and Rohan's completion time in the hypothesis contradict the premise
    label = "contradiction"
elif rohit_days_hypothesis!= rohit_days_premise or rohan_days_hypothesis!= rohan_days_premise:
    # check if the number of days taken by either Rohit or Rohan in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
