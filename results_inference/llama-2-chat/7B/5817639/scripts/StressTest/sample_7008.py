male_count_premise = 25
male_count_hypothesis = 45

# the hypothesis refers to the number of males, which is also mentioned in the premise
if male_count_hypothesis <= male_count_premise:
    # check if the estimate of'male_count_hypothesis' contradicts the number of males in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males less than'male_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
