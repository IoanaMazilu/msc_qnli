shoes_premise = 25
shoes_hypothesis = 65

# the hypothesis talks about the number of pairs of shoes that Marcella has, referenced also in the premise
if shoes_premise >= shoes_hypothesis:
    # check if the number of pairs of shoes in the premise contradicts the estimate of less than 'shoes_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the number of pairs of shoes
    # any number of pairs of shoes less than 'shoes_hypothesis' is consistent with the premise, but can be explicitly entailed from the premise
    label = "entailment"

print(label)
