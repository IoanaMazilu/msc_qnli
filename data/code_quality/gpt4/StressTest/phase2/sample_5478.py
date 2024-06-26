voted_premise = 3
voted_hypothesis = 5

# the hypothesis refers to the number of people who voted to watch My Hero Academia Academia in the premise
if voted_premise >= voted_hypothesis:
    # check if the number of people who voted in the premise contradicts the hypothesis estimate of less than 'voted_hypothesis'
    label = "contradiction"
elif voted_premise != voted_hypothesis:
    # check if the number of people who voted in the premise contradicts the exact number of 'voted_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the premise number of people who voted does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
