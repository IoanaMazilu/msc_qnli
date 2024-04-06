# Premise: Instagram got so popular so fast that Facebook took notice and purchased the company for a billion dollars -- (yes, $1 billion) -- to bolster its own smart phone presence shortly before its IPO.
# Hypothesis: Rushkoff:Facebook paid $1 billion for Instagram and needs a return.
# Golden Label: neutral

purchase_price_premise = 1000000000
purchase_price_hypothesis = 1000000000

# the hypothesis mentions the purchase price of Instagram by Facebook, which is also mentioned in the premise
if purchase_price_hypothesis != purchase_price_premise:
    # check if the purchase price in the hypothesis contradicts the purchase price reported in the premise
    label = "contradiction"
else:
    # if the purchase price in the hypothesis does not contradict the premise, it remains neutral or entailment
    # the hypothesis also mentions a need for return, which cannot be entailed from the premise
    label = "neutral"

print(label)

