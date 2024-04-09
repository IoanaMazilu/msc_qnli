train_leaves_delhi_premise = "more than 4 a"
train_leaves_delhi_hypothesis = 9

# define variables with representative names for the numerical entities in both inputs
train_leaves_delhi_premise_value = float(train_leaves_delhi_premise.split(" a")[0])
train_leaves_delhi_hypothesis_value = float(train_leaves_delhi_hypothesis.split(" a")[0])

# extract all quantities as valid numbers (integers or floats)
if train_leaves_delhi_premise_value > train_leaves_delhi_hypothesis_value:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif train_leaves_delhi_premise_value == train_leaves_delhi_hypothesis_value:
    # the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise value is an estimate, and the hypothesis value is greater than the estimate
    label = "entailment"

print(label)
