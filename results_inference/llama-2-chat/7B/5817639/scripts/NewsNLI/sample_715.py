labels = ["entailment", "contradiction", "neutral"]

tip_premise = 10000 # number of tips received from the premise
tip_hypothesis = 562435 # phone number of the anonymous tip line in the hypothesis

# the hypothesis mentions a different phone number for anonymous tips than the premise
if tip_hypothesis!= tip_premise:
    # check if the phone number in the hypothesis contradicts the phone number in the premise
    label = "contradiction"
else:
    # if the phone number in the hypothesis matches the phone number in the premise, we can infer entailment
    label = "entailment"

print(label)
