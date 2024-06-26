labels = ["entailment"]

# the hypothesis and premise mention the Fed raising rates and the number of expected future hikes
if "Fed raises rates again" in hypothesis:
    # check if the hypothesis matches the premise verbatim
    label = "entailment"
else:
    # if the hypothesis does not match the premise verbatim, we cannot infer entailment
    label = "neutral"

print(labels)
