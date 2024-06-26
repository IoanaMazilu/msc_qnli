participants_premise = 4
participants_hypothesis = 3

# the hypothesis mentions the number of participants in a race, as stated in the premise
if participants_hypothesis >= participants_premise:
    # check if the number of participants in hypothesis contradicts the estimate of less than 'participants_premise'
    label = "contradiction"
elif participants_hypothesis < participants_premise:
    # if the number of participants in the hypothesis is less than 'participants_premise', we can infer entailment
    label = "entailment"

print(label)
