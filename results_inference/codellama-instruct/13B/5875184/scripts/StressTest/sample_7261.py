premise = "If Carol's rectangle measures less than 52 inches by 15 inches and Jordan's rectangle is 9 inches long, how wide is Jordan's rectangle, in inches?"
hypothesis = "If Carol's rectangle measures 12 inches by 15 inches and Jordan's rectangle is 9 inches long, how wide is Jordan's rectangle, in inches?"

# extract the numerical entities from the premise and hypothesis
premise_width = 52
premise_length = 15
hypothesis_width = 12
hypothesis_length = 15

# check if the hypothesis value contradicts the premise value
if hypothesis_width < premise_width:
    label = "contradiction"
elif hypothesis_length!= premise_length:
    label = "contradiction"
else:
    label = "neutral"

print(label)
