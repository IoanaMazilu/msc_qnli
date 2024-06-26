man_dollars_premise = 1000
man_dollars_hypothesis = 1000

# the hypothesis talks about the same amount of money as the premise
if man_dollars_hypothesis!= man_dollars_premise:
    # check if the hypothesis value contradicts the estimate of'man_dollars_premise'
    label = "contradiction"
else:
    # the premise and hypothesis are consistent
    label = "entailment"

print(label)
