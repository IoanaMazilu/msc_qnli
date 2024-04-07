# Premise: Robert ate more than 5 chocolates, Nickel ate 3 chocolates.
# Hypothesis: Robert ate 7 chocolates, Nickel ate 3 chocolates.
# Golden Label: neutral

chocolates_robert_premise = 5
chocolates_robert_hypothesis = 7
chocolates_nickel_premise = 3
chocolates_nickel_hypothesis = 3

# the hypothesis talks about the number of chocolates consumed by Robert and Nickel, referenced also in the premise
if chocolates_robert_hypothesis <= chocolates_robert_premise:
    # check if the number of chocolates Robert ate in the hypothesis contradicts the estimate of more than 'chocolates_robert_premise'
    label = "contradiction"
elif chocolates_nickel_hypothesis != chocolates_nickel_premise:
    # check if the number of chocolates Nickel ate in the hypothesis contradicts the number of chocolates Nickel ate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chocolates Robert ate
    # any number of chocolates greater than 'chocolates_robert_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

