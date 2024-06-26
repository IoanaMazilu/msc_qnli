# The premise gives the area of the land as 120 square feet each side
area_premise = 120
# The hypothesis gives the area of the land as less than 320 square feet each side
area_hypothesis = 320

if area_premise >= area_hypothesis:
    # If the area of the land in the premise is greater than or equal to the area of the land in the hypothesis,
    # then the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the area of the land in the premise is less than the area of the land in the hypothesis,
    # then the premise entails the hypothesis
    label = "entailment"

print(label)
