mpg_premise = 32
mpg_hypothesis = 62

# the hypothesis refers to the number of miles per gallon that Dan's car gets
if mpg_hypothesis >= mpg_premise:
    # check if the hypothesis value contradicts the number of miles per gallon in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the number of miles per gallon
    # any value less than'mpg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
