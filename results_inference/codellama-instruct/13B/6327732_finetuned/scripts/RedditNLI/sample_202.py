premise = "No there is not a $2 TRILLION error in the budget."
hypothesis = "Trump Budget Based on $2 Trillion Math Error."

# extract the numerical entities from the premise and hypothesis
premise_amount = float(premise.split("$")[1].split(" ")[0])
hypothesis_amount = float(hypothesis.split("$")[1].split(" ")[0])

# check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
