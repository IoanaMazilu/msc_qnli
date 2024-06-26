dogs_premise = 5
cats_premise = 6
dogs_hypothesis = 5
cats_hypothesis = 6

# the hypothesis refers to the number of dogs and cats Martha has, as given in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the hypothesis value contradicts the exact number of dogs in the premise
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the exact number of cats in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
