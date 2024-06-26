returned_tshirts_premise = 4
returned_tshirts_hypothesis = 8

if returned_tshirts_hypothesis <= returned_tshirts_premise:
    # check if the number of returned t-shirts in the hypothesis contradicts the number of returned t-shirts reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of returned t-shirts
    # any number of returned t-shirts greater than'returned_tshirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
