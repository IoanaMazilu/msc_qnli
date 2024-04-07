# Premise: Kishore saved 10% of his monthly salary.
# Hypothesis: Kishore saved less than 10% of his monthly salary.
# Golden Label: contradiction

percentage_saved_premise = 10
percentage_saved_hypothesis = 10

# the hypothesis talks about the percentage of salary Kishore saved, which is also referenced in the premise
if percentage_saved_hypothesis >= percentage_saved_premise:
    # check if the hypothesis value contradicts the premise which states Kishore saved exact 'percentage_saved_premise' percent
    label = "contradiction"
else:
    # if the hypothesis value is less than 'percentage_saved_premise', it can be entailed from the premise
    label = "entailment"

print(label)

