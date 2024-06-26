cement_weight_premise = 750
cement_weight_hypothesis = 350

# the hypothesis talks about the weight of cement Tim has, referenced also in the premise
if cement_weight_hypothesis >= cement_weight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cement_weight_premise'
    label = "contradiction"
else:
    # if the hypothesis value doesn't contradict the premise, then we can infer entailment, 
    # because the premise explicitly states that the weight of cement is less than 'cement_weight_premise'
    label = "entailment"

print(label)
