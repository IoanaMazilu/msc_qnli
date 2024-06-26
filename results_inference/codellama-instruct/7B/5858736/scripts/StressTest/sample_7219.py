lena_grade_premise = 30
lena_grade_hypothesis = 80

# the hypothesis talks about the percentage of grades in Lena's class
if lena_grade_hypothesis <= lena_grade_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lena_grade_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of grades in Lena's class
    # any percentage greater than 'lena_grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
