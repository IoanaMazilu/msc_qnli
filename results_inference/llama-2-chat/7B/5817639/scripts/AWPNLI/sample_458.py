height_premise = 0.5  # height of one sandcastle in the premise
height_hypothesis = 1.33333333333  # total height of both sandcastles in the hypothesis

# compare the height of the sandcastles in the hypothesis to the height in the premise
if height_hypothesis == height_premise:
    # if the height of the sandcastles matches, we can infer entailment
    label = "entailment"
else:
    # if the height of the sandcastles contradicts, we can infer contradiction
    label = "contradiction"

print(label)
