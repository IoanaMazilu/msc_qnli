# Premise: Sony and Johnny caught less than 70 fishes.
# Hypothesis: Sony and Johnny caught 50 fishes.
# Golden Label: neutral

fishes_caught_premise = 70
fishes_caught_hypothesis = 50

# the hypothesis talks about the number of fishes caught by Sony and Johnny, referenced also in the premise
if fishes_caught_hypothesis >= fishes_caught_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fishes_caught_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fishes
    # any number of fishes less than 'fishes_caught_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

