cans_premise = 8
cans_hypothesis = 4

# the hypothesis refers to the number of paint cans Diane uses to paint one third of her room, also mentioned in the premise
if cans_hypothesis >= cans_premise:
    # check if the number of 'cans_hypothesis' contradicts the estimate of less than 'cans_premise'
    label = "contradiction"
elif cans_hypothesis < cans_premise:
    # if the number of 'cans_hypothesis' is less than 'cans_premise', it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
