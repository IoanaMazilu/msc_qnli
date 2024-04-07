# Premise: The average length of the sides of triangle ABC is less than 72.
# Hypothesis: The average length of the sides of triangle ABC is 12.
# Golden Label: neutral

average_length_sides_premise = 72
average_length_sides_hypothesis = 12

# the hypothesis refers to the average length of the sides of a triangle, which is also referred to in the premise
if average_length_sides_hypothesis >= average_length_sides_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_length_sides_premise'
    label = "contradiction"
elif average_length_sides_hypothesis <= 0:
    # check if the hypothesis value contradicts the real-world fact that lengths are positive
    label = "contradiction"
else:
    # the premise gives only an estimate cap for the average length of the triangle sides
    # any average length less than 'average_length_sides_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

