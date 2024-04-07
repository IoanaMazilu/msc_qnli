# Premise: If the perimeter of Δ ACD is more than 3 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Hypothesis: If the perimeter of Δ ACD is 9 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Golden Label: neutral

perimeter_acd_premise = 3 + 3 * (3 ** 0.5)
perimeter_acd_hypothesis = 9 + 3 * (3 ** 0.5)

# the hypothesis talks about the perimeter of Δ ACD, which is also mentioned in the premise
if perimeter_acd_hypothesis <= perimeter_acd_premise:
    # check if the hypothesis value contradicts the estimate of more than 'perimeter_acd_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the perimeter of Δ ACD
    # any value of perimeter greater than 'perimeter_acd_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

