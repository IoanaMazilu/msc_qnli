males_total_premise = 25
males_total_hypothesis = 45

# the hypothesis refers to the total number of males, which is also mentioned in the premise
if males_total_hypothesis <= males_total_premise:
    # check if the hypothesis value contradicts the estimate of less than'males_total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of males
    # any total number of males less than'males_total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
