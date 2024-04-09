iron_coins_premise = 2
copper_coins_premise = 5
more_than_2_premise = False

# define variables with representative names for the numerical entities in both inputs
iron_coins_hypothesis = 10
copper_coins_hypothesis = 15
more_than_2_hypothesis = True

# extract all quantities as valid numbers (integers or floats)
iron_coins_premise = int(iron_coins_premise)
copper_coins_premise = int(copper_coins_premise)
more_than_2_premise = bool(more_than_2_premise)

# compare the variables and determine the label
if more_than_2_hypothesis and (iron_coins_hypothesis > iron_coins_premise or copper_coins_hypothesis > copper_coins_premise):
    # the hypothesis refers to the number of coins of each type, which is more than the premise
    label = "entailment"
elif more_than_2_premise and not (iron_coins_hypothesis > iron_coins_premise or copper_coins_hypothesis > copper_coins_premise):
    # the premise gives only an estimate for the number of coins of each type, and the hypothesis does not contradict it
    label = "neutral"
else:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
