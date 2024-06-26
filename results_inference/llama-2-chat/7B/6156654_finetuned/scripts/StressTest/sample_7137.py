saving_decrease_premise = 10
saving_decrease_hypothesis = 60

# the hypothesis talks about the decrease in the saving amount, which is also mentioned in the premise
if saving_decrease_hypothesis <= saving_decrease_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is an entailment
    label = "entailment"

print(label)
