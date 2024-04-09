torture_premise = "confessions'apparently obtained under torture."
torture_hypothesis = "Three executed men apparently confessed under torture, Human Rights Watch says."

# define variables with representative names for the numerical entities in both inputs
torture_premise_value = len(torture_premise.split())
torture_hypothesis_value = len(torture_hypothesis.split())

# extract all quantities as valid numbers (integers or floats)
torture_premise_value_int = int(torture_premise_value)
torture_hypothesis_value_int = int(torture_hypothesis_value)

# compare the values of the variables
if torture_premise_value_int == torture_hypothesis_value_int:
    # if the values are the same, we can infer entailment
    label = "entailment"
elif torture_premise_value_int!= torture_hypothesis_value_int:
    # if the values are different, we can infer contradiction
    label = "contradiction"
else:
    # if the values are different but we cannot infer entailment or contradiction, we can label as neutral
    label = "neutral"

print(label)
