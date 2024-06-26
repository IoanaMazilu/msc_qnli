  sold_premise = 750
  sold_hypothesis = 450

  # the hypothesis refers to the amount sold, which is also mentioned in the premise
  if sold_hypothesis >= sold_premise:
    # check if the hypothesis value contradicts the estimate of less than'sold_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount sold
    # any amount less than'sold_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
