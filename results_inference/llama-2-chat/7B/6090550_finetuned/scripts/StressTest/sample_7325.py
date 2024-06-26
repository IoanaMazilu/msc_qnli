sentsimple_premise = 1
sentsimple_hypothesis = 5

# the hypothesis talks about the number of times Rikki goes to the gym after a certain number of weeks, referenced also in the premise
if sentsimple_hypothesis!= sentsimple_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
