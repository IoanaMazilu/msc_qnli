tickets_premise = 10
tickets_hypothesis = 60

# the hypothesis talks about the number of concert tickets Martin bought, which is also referred to in the premise
if tickets_hypothesis == tickets_premise:
    # check if the number of tickets in the hypothesis matches the number of tickets in the premise
    label = "entailment"
elif tickets_hypothesis < tickets_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets in the premise
    label = "contradiction"
else:
    # the number of tickets in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
