# Premise: Sanoop bought more than 2 t-shirts at an average price (arithmetic mean) of Rs.
# Hypothesis: Sanoop bought 8 t-shirts at an average price (arithmetic mean) of Rs.
# Golden Label: neutral

tshirts_bought_premise = 2
tshirts_bought_hypothesis = 8

# the hypothesis specifies the number of t-shirts bought by Sanoop, also mentioned in the premise
if tshirts_bought_hypothesis <= tshirts_bought_premise:
    # check if the number of t-shirts bought in the hypothesis contradicts the premise estimate of more than 'tshirts_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts
    # any number of t-shirts greater than 'tshirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

