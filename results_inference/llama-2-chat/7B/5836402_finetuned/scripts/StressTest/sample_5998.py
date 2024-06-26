lists_premise = 4/4
lists_hypothesis = 1/4

# the hypothesis refers to the number of lists the film must appear in for consideration, as stated in the premise
if lists_hypothesis >= lists_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lists_premise'
    label = "contradiction"
elif lists_hypothesis < lists_premise:
    # if the hypothesis value is less than the premise one, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
