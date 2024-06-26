rd_ranking_premise = 65
rd_ranking_hypothesis = 15
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis refers to the ranking of Veena in the class, also referenced in the premise
if rd_ranking_hypothesis >= rd_ranking_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rd_ranking_premise'
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the number of students in the class in the hypothesis contradicts the number of students in the class reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ranking of Veena
    # any ranking greater than 'rd_ranking_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
