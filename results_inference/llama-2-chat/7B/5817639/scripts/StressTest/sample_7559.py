shoes_premise = 25
shoes_hypothesis = 25

# the hypothesis talks about the number of shoes owned by Marcella, which is also mentioned in the premise
if shoes_hypothesis <= shoes_premise:
    # check if the hypothesis value contradicts the estimate of'shoes_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of shoes, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
