# Premise: Kishore saved 10% of his monthly salary.
# Hypothesis: Kishore saved more than 10% of his monthly salary.
# Golden Label: contradiction

saved_percentage_premise = 10
saved_percentage_hypothesis = 10

# the hypothesis talks about the percentage of monthly salary Kishore saved, referenced also in the premise
if saved_percentage_hypothesis <= saved_percentage_premise:
    # check if the hypothesis value contradicts the estimate of more than 'saved_percentage_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact value for the percentage of salary saved
    # any percentage greater than 'saved_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

