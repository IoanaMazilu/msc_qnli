# Premise: Mike buys 3 cartons of eggs at the store.
# Hypothesis: Mike buys less than 8 cartons of eggs at the store.
# Golden Label: entailment

cartons_eggs_premise = 3
cartons_eggs_hypothesis = 8

# the hypothesis talks about the number of egg cartons bought by Mike, referenced also in the premise
if cartons_eggs_premise >= cartons_eggs_hypothesis:
    # check if the number of egg cartons in the premise contradicts the estimate of less than 'cartons_eggs_hypothesis'
    label = "contradiction"
else:
    # if the number of egg cartons in the premise does not contradict the estimate of less than 'cartons_eggs_hypothesis', we can infer entailment
    label = "entailment"

print(label)

