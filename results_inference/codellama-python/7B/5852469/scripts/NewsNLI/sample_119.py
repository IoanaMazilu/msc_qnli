age_premise = 19
age_hypothesis = 19
major_premise = "computer science"
major_hypothesis = "computer science"
university_premise = "University of California, Berkeley"
university_hypothesis = "University of California, Berkeley"

# the hypothesis mentions the same information as the premise
if age_hypothesis!= age_premise:
    # check if the age from the hypothesis contradicts the age in the premise
    label = "contradiction"
elif major_hypothesis!= major_premise:
    # check if the major from the hypothesis contradicts the major in the premise
    label = "contradiction"
elif university_hypothesis!= university_premise:
    # check if the university from the hypothesis contradicts the university in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
