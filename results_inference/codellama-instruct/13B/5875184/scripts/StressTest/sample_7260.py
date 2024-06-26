premise = "If Carol's rectangle measures 12 inches by 15 inches and Jordan's rectangle is 9 inches long, how wide is Jordan's rectangle, in inches?"
hypothesis = "If Carol's rectangle measures less than 52 inches by 15 inches and Jordan's rectangle is 9 inches long, how wide is Jordan's rectangle, in inches?"

# extract the numerical entities from the premise and hypothesis
premise_width = 12
premise_length = 15
hypothesis_width = 52
hypothesis_length = 15

# compare the width of the rectangles
if premise_width < hypothesis_width:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif premise_length!= hypothesis_length:
    # the number of inches in the hypothesis is different from the number of inches in the premise
    label = "neutral"
else:
    # the hypothesis value is consistent with the premise value
    label = "entailment"

print(label)
