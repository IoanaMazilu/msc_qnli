offer_premise = 32
offer_hypothesis = 52

# The hypothesis talks about the offer percentage on shirts, which is also mentioned in the premise
if offer_hypothesis <= offer_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif offer_hypothesis > offer_premise:
    # The hypothesis value is greater than the premise, but it does not contradict the premise. However, it can't be explicitly entailed from the premise
    label = "neutral"

print(label)
