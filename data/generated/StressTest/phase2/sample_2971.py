# Premise: A circle of radius less than 30 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Hypothesis: A circle of radius 10 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Golden Label: neutral

circle_radius_premise = 30
circle_radius_hypothesis = 10

# The hypothesis mentions a circle with a specific radius, which is also referenced in the premise
if circle_radius_hypothesis >= circle_radius_premise:
    # Check if the hypothesis value contradicts the premise which states that the radius is less than 'circle_radius_premise'
    label = "contradiction"
elif circle_radius_hypothesis < circle_radius_premise:
    # If the radius in the hypothesis is less than 'circle_radius_premise', it is consistent with the premise
    # Thus, the premise entails the hypothesis
    label = "entailment"

print(label)

