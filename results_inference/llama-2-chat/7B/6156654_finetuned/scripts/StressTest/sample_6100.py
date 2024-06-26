days_premise = 86
days_hypothesis = 16

# the hypothesis talks about the number of days Mary needs to complete a task, which is also mentioned in the premise
if days_hypothesis >= days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif days_hypothesis < days_premise:
    # check if the hypothesis value is less than the premise value
    # this means that the hypothesis is entailed by the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutral
    label = "neutral"

print(label)
