premise = "California Gov. Jerry Brown approves minimum wage increase to $15."
hypothesis = "California Is About to Make a $15 Minimum Wage a Reality."

# extract the numerical entities from the premise and hypothesis
premise_amount = float(premise.split("$")[1])
hypothesis_amount = float(hypothesis.split("$")[1])

# check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount > premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
