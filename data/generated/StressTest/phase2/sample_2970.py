# Premise: A circle of radius 10 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Hypothesis: A circle of radius less than 30 inches has its center at the vertex C of an equilateral triangle ABC and passes through the other two vertices.
# Golden Label: entailment

circle_radius_premise = 10
circle_radius_hypothesis = 30

# the hypothesis talks about the radius of a circle that passes through the vertices of a triangle, as mentioned in the premise
if circle_radius_premise >= circle_radius_hypothesis:
    # check if the premise's circle radius contradicts the estimate of less than 'circle_radius_hypothesis'
    label = "contradiction"
elif circle_radius_premise < circle_radius_hypothesis:
    # the premise explicitly states the circle radius
    # if 'circle_radius_premise' is less than 'circle_radius_hypothesis' it is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)

