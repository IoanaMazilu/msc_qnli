john_tip_premise = 15
john_tip_hypothesis = 15

# the hypothesis talks about the tip John paid, referenced also in the premise
if john_tip_hypothesis <= john_tip_premise:
    # check if the hypothesis value contradicts the exact tip percent 'john_tip_premise'
    label = "contradiction"
else:
    # the premise gives only an exact value for the tip percent
    # any tip percent greater than 'john_tip_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
