# Define variables for the premise and hypothesis
students_random_premise = 112
students_scramjet_premise = 234
students_both_premise = 112
students_random_hypothesis = 312
students_scramjet_hypothesis = 234
students_both_hypothesis = 112

# Check if the hypothesis values contradict the premise
if students_random_hypothesis > students_random_premise:
    label = "contradiction"
elif students_scramjet_hypothesis > students_scramjet_premise:
    label = "contradiction"
elif students_both_hypothesis > students_both_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
