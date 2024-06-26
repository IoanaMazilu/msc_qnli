shoes_premise = 24
shoes_hypothesis = 44

# the hypothesis talks about the number of shoes Marcella has, referenced also in the premise
if shoes_premise >= shoes_hypothesis:
    # check if the number of shoes in the premise contradicts the estimate of less than 'shoes_hypothesis'
    label = "contradiction"
else:
    # the number of shoes Marcella has, as stated in the premise, is less than 'shoes_hypothesis'
    # thus, the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
