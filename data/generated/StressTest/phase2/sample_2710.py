# Premise: Mike buys less than 8 cartons of eggs at the store.
# Hypothesis: Mike buys 3 cartons of eggs at the store.
# Golden Label: neutral

cartons_eggs_premise = 8
cartons_eggs_hypothesis = 3

# the hypothesis talks about the number of egg cartons Mike buys, referenced also in the premise
if cartons_eggs_hypothesis >= cartons_eggs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cartons_eggs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cartons
    # any number of cartons less than 'cartons_eggs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

