premise = "Nitin ranks 15 th in a class of 47 students."
hypothesis = "Nitin ranks less than 75 th in a class of 47 students."

# extract the numerical entities from the premise
rank_premise = 15
total_students_premise = 47

# extract the numerical entities from the hypothesis
rank_hypothesis = 75
total_students_hypothesis = 47

# check if the hypothesis value contradicts the premise
if rank_hypothesis <= rank_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
