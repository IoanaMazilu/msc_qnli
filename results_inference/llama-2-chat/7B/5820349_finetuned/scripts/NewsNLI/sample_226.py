japanese_descent_people_premise = 1800000
japanese_descent_people_hypothesis = 1800000

# the hypothesis mentions the number of Japanese descent people in Brazil, which is also referenced in the premise
if japanese_descent_people_hypothesis!= japanese_descent_people_premise:
    # check if the number of Japanese descent people in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of Japanese descent people in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
