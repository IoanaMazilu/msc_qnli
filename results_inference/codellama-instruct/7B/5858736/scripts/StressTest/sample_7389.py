rosy_premise = 10
mary_premise = 100
rosy_hypothesis = 30
mary_hypothesis = 100

# the hypothesis talks about the efficiency of Rosy and Mary, referenced also in the premise
if rosy_hypothesis >= rosy_premise:
    # check if the hypothesis value contradicts the estimate of 'rosy_premise'
    label = "contradiction"
elif mary_hypothesis >= mary_premise:
    # check if the hypothesis value contradicts the estimate of'mary_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
