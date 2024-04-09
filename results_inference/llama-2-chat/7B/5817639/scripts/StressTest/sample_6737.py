rohit_days_premise = 12
rohit_days_hypothesis = 62
rohan_days_premise = 6
rohan_days_hypothesis = 6

# the hypothesis talks about the time taken by Rohit and Rohan to complete a work, referenced also in the premise
if rohit_days_hypothesis >= rohit_days_premise:
    # check if the hypothesis value contradicts the estimate of 'rohit_days_premise'
    label = "contradiction"
elif rohan_days_hypothesis >= rohan_days_premise:
    # check if the hypothesis value contradicts the estimate of 'rohan_days_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
