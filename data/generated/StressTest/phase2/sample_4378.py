# Premise: less than 321, 144, 169, 196, 225, 256, 288, 324, 361.
# Hypothesis: 121, 144, 169, 196, 225, 256, 288, 324, 361.
# Golden Label: neutral

numbers_premise = 321
numbers_hypothesis = 121

# the hypothesis refers to a number also mentioned in the premise
if numbers_hypothesis >= numbers_premise:
    # check if the hypothesis contradicts the premise of having numbers less than 'numbers_premise'
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

