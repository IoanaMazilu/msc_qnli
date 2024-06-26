amount_premise = 100000
amount_hypothesis = 100000

# the hypothesis talks about the amount of money invested by Raviraj, which is the same as the amount of money invested in the premise
if amount_premise!= amount_hypothesis:
    # check if the hypothesis value contradicts the amount of money invested in the premise
    label = "contradiction"
else:
    # the premise and hypothesis talk about the same amount of money invested by Raviraj
    label = "entailment"

print(label)
