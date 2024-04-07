# Premise: Sony and Johnny caught 25 fishes.
# Hypothesis: Sony and Johnny caught less than 75 fishes.
# Golden Label: entailment

fishes_caught_premise = 25
fishes_caught_hypothesis = 75

# the hypothesis talks about the number of fishes caught by Sony and Johnny, as referenced in the premise
if fishes_caught_premise >= fishes_caught_hypothesis:
    # check if the number of fishes caught in the premise contradicts the estimate of less than 'fishes_caught_hypothesis'
    label = "contradiction"
else:
    # the number of fishes caught in the premise is less than 'fishes_caught_hypothesis' and does not contradict the hypothesis
    # however, the hypothesis can be fully and explicitly entailed from the premise since the premise number is within the range of the hypothesis
    label = "entailment"

print(label)

