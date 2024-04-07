# Premise: Rob has more than 5 toy trucks.
# Hypothesis: Rob has 8 toy trucks.
# Golden Label: neutral

toy_trucks_premise = 5
toy_trucks_hypothesis = 8

# the hypothesis talks about the number of toy trucks Rob has, referenced also in the premise
if toy_trucks_hypothesis <= toy_trucks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'toy_trucks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of toy trucks
    # any number of toy trucks greater than 'toy_trucks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

