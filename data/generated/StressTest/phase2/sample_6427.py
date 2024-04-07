# Premise: less than 750 and she sold that to George for Rs.
# Hypothesis: 450 and she sold that to George for Rs.
# Golden Label: neutral

sold_to_george_premise = 750
sold_to_george_hypothesis = 450

# the hypothesis talks about the amount sold to George, referenced also in the premise
if sold_to_george_hypothesis >= sold_to_george_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sold_to_george_premise'
    label = "contradiction"
elif sold_to_george_hypothesis < sold_to_george_premise:
    # the premise gives an estimate for the amount sold to George
    # any amount less than 'sold_to_george_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

