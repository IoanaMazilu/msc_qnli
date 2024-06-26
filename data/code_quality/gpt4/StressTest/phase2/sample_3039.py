passing_percentage_premise = 80
passing_percentage_hypothesis = 10
marks_obtained = 200
marks_failed_by = 200

# the hypothesis and premise both refer to the passing percentage in Martin's exam and the marks he obtained
if passing_percentage_hypothesis > passing_percentage_premise:
    # check if the passing percentage in the hypothesis contradicts the passing percentage in the premise
    label = "contradiction"
else:
    # even if the passing percentage in the hypothesis is less than or equal to the percentage in the premise, 
    # the exact passing mark cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
