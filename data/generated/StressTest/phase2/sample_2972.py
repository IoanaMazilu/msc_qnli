# Premise: A circle of radius 10 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Hypothesis: A circle of radius less than 10 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Golden Label: contradiction

circle_radius_premise = 10
circle_radius_hypothesis = 10

# the hypothesis refers to the circle radius described in the premise
if circle_radius_hypothesis < circle_radius_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif circle_radius_hypothesis >= circle_radius_premise:
    # check if the hypothesis value can be explicitly entailed from the premise
    label = "entailment"

print(label)

