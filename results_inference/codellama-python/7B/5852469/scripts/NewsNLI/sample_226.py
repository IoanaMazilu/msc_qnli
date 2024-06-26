people_of_japanese_descent_premise = 1800000
people_of_japanese_descent_hypothesis = 1800000

# the hypothesis mentions the number of people of Japanese descent in Brazil, which is also mentioned in the premise
if people_of_japanese_descent_hypothesis!= people_of_japanese_descent_premise:
    # check if the number of people of Japanese descent from the hypothesis contradicts the number of people of Japanese descent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
