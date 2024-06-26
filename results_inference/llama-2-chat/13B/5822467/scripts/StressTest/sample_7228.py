# define variables with representative names for the numerical entities in both inputs
nancy_marks_premise = [86, 75, 52, 68, 89]
nancy_marks_hypothesis = [66, 75, 52, 68, 89]

# extract all quantities as valid numbers (integers or floats)
nancy_marks_premise_ints = [int(x) for x in nancy_marks_premise]
nancy_marks_hypothesis_ints = [int(x) for x in nancy_marks_hypothesis]

# compare the variables
if all(x <= y for x, y in zip(nancy_marks_premise_ints, nancy_marks_hypothesis_ints)):
    # if the hypothesis values are all less than or equal to the premise values, we can infer entailment
    label = "entailment"
elif any(x!= y for x, y in zip(nancy_marks_premise_ints, nancy_marks_hypothesis_ints)):
    # if the hypothesis values contradict the premise values, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
