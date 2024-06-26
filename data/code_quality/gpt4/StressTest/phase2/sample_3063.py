# Establishing variables for Albert's age in relation to Mary's and Betty's age
albert_mary_relation_premise = 2
albert_betty_relation_premise = 4
albert_mary_relation_hypothesis = 4
albert_betty_relation_hypothesis = 4

# Comparing Albert's age in relation to Mary
if albert_mary_relation_hypothesis <= albert_mary_relation_premise:
    # If Albert's age in hypothesis is less than or equal to Albert's age in the premise in relation to Mary's age
    label_mary = "entailment"
else:
    # If Albert's age in hypothesis is greater than Albert's age in the premise in relation to Mary's age
    label_mary = "contradiction"

# Comparing Albert's age in relation to Betty
if albert_betty_relation_hypothesis != albert_betty_relation_premise:
    # If Albert's age in hypothesis is not equal to Albert's age in the premise in relation to Betty's age
    label_betty = "contradiction"
else:
    # If Albert's age in hypothesis is equal to Albert's age in the premise in relation to Betty's age
    label_betty = "entailment"

# If either of the comparisons is a contradiction, then the overall result is a contradiction
if label_mary == "contradiction" or label_betty == "contradiction":
    label = "contradiction"
# If both comparisons are entailment, then the overall result is an entailment
elif label_mary == "entailment" and label_betty == "entailment":
    label = "entailment"
# If neither of the above conditions are met, then the result is neutral
else:
    label = "neutral"

print(label)
