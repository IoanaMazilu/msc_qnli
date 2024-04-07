# Premise: Nitin ranks less than 82 th in a class of 56 students.
# Hypothesis: Nitin ranks 12 th in a class of 56 students.
# Golden Label: neutral

nitin_rank_premise = 82
nitin_rank_hypothesis = 12
students_count = 56

# the hypothesis talks about Nitin's rank in a class, referenced also in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the rank in the hypothesis contradicts the rank in the premise
    label = "contradiction"
elif nitin_rank_hypothesis > students_count:
    # check if the rank in the hypothesis contradicts the class size
    label = "contradiction"
else:
    # Nitin's rank in the hypothesis is less than the premise and within the class size, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

