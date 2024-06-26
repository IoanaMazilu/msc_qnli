saving_premise = 10
saving_hypothesis = 6

# the hypothesis talks about the percentage of decrease in David's Bank's saving, which is also mentioned in the premise
if saving_hypothesis <= saving_premise * 0.6:
    # check if the hypothesis value contradicts the estimate of less than'saving_premise * 0.6'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of decrease, which is consistent with the hypothesis
    label = "entailment"

print(label)
