premise = "Gold tops $1,500 for first time."
hypothesis = "Gold tops $1500/oz for he first time."

# the hypothesis and premise mention the price of gold
if premise.endswith("for first time"):
    # check if the premise mentions the price of gold for the first time
    label = "entailment"
else:
    # the premise does not mention the price of gold for the first time
    label = "neutral"

print(label)
