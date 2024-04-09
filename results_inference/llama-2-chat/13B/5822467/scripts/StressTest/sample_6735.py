rohit_days_premise = 12
rohit_days_hypothesis = 6
rohan_days_premise = 6
rohan_days_hypothesis = 6

# the hypothesis refers to the number of days taken by Rohit and Rohan to complete the work
if rohit_days_premise <= rohit_days_hypothesis and rohan_days_premise <= rohan_days_hypothesis:
    # check if the estimate of 'rohit_days_hypothesis' and 'rohan_days_hypothesis' do not contradict the premise
    label = "entailment"
elif rohit_days_hypothesis > rohit_days_premise or rohan_days_hypothesis > rohan_days_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
