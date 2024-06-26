bookman_purchased_premise = 60
bookman_purchased_hypothesis = 40

# the hypothesis refers to the number of copies purchased by Bookman
if bookman_purchased_hypothesis <= bookman_purchased_premise:
    # check if the estimate of 'bookman_purchased_hypothesis' contradicts the number of copies purchased by Bookman
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of copies purchased by Bookman
    # any number of copies greater than 'bookman_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
