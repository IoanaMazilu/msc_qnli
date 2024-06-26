num_girls_premise = 2
num_girls_hypothesis = 1
num_boys_premise = 2
num_boys_hypothesis = 2

# the hypothesis refers to the number of girls mentioned in the premise
if num_girls_hypothesis >= num_girls_premise:
    # check if the hypothesis value contradicts the number of girls in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of girls, but the hypothesis gives a lower bound
    # any number of possible ways for the girls to go on a date with the boys is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
