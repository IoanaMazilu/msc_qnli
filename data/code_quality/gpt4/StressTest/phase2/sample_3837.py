alice_leaves_premise = 30
alice_leaves_hypothesis = 50

# the hypothesis talks about the time Alice leaves City A after Bob, referenced also in the premise
if alice_leaves_premise > alice_leaves_hypothesis:
    # check if the premise value contradicts the estimate of less than 'alice_leaves_hypothesis'
    label = "contradiction"
elif alice_leaves_premise < alice_leaves_hypothesis:
    # check if the premise value is less than the estimate of 'alice_leaves_hypothesis'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
