class_size_premise = 59
class_size_hypothesis = 59
min_clubs_premise = 1
max_clubs_premise = 3
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# the hypothesis refers to the number of members in the class and the number of clubs they can sign up for
if class_size_hypothesis <= class_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'class_size_premise'
    label = "contradiction"
elif min_clubs_hypothesis!= min_clubs_premise or max_clubs_hypothesis!= max_clubs_premise:
    # check if the minimum and maximum number of clubs in the hypothesis contradict the minimum and maximum number of clubs mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
