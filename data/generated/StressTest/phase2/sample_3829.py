# Premise: Latha has less than 20 candies, ramu has 20 candies.
# Hypothesis: Latha has 10 candies, ramu has 20 candies.
# Golden Label: neutral

latha_candies_premise = 20
ramu_candies_premise = 20
latha_candies_hypothesis = 10
ramu_candies_hypothesis = 20

# the hypothesis refers to the number of candies Latha and Ramu have, mentioned in the premise
if latha_candies_hypothesis >= latha_candies_premise:
    # check if the number of candies Latha has in the hypothesis contradicts the estimate of less than 'latha_candies_premise'
    label = "contradiction"
elif ramu_candies_hypothesis != ramu_candies_premise:
    # check if the number of candies Ramu has in the hypothesis contradicts the number of candies Ramu has in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of candies Latha has
    # any number of candies less than 'latha_candies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

