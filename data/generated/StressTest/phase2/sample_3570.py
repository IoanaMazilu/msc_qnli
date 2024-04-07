# Premise: If the perimeter of Δ ACD is 9 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Hypothesis: If the perimeter of Δ ACD is more than 3 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Golden Label: entailment

perimeter_ACD_premise = 9 + 3 * (3 ** 0.5)
perimeter_ACD_hypothesis = 3 + 3 * (3 ** 0.5)

# The hypothesis talks about the perimeter of triangle ACD, also mentioned in the premise
if perimeter_ACD_premise <= perimeter_ACD_hypothesis:
    # Check if the value of 'perimeter_ACD_premise' contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # The premise and hypothesis are discussing about the same perimeters
    # Any perimeter value for triangle ACD greater than 'perimeter_ACD_hypothesis' is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"

print(label)

