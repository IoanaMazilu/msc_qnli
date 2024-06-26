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
elif min_clubs_hypothesis < min_clubs_premise or max_clubs_hypothesis > max_clubs_premise:
    # check if the number of clubs in the hypothesis contradicts the number of clubs mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members and the number of clubs they can sign up for
    # any number of members greater than 'class_size_premise' and any number of clubs between'min_clubs_premise' and'max_clubs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
