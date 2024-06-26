# Define variables with representative names for the numerical entities in both inputs
students_random_premise = 302
students_scramjet_premise = 232
students_both_premise = 112
students_random_hypothesis = 102
students_scramjet_hypothesis = 232
students_both_hypothesis = 112

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis values and estimates do not contradict the premise ones
if students_random_hypothesis <= students_random_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
