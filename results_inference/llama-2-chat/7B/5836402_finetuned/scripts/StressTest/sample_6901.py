offer_premise = 70
offer_hypothesis = 30

# the hypothesis refers to the offer for shirts mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer in the hypothesis contradicts the offer in the premise
    label = "contradiction"
else:
    # if the offer in the hypothesis is less than the offer in the premise, it is a contradiction
    label = "contradiction"

print(label)
