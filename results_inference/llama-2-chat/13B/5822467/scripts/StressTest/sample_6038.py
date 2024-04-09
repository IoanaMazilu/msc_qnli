members_premise = 59
academic_clubs_premise = 1
members_hypothesis = 100
academic_clubs_hypothesis = 3

# the hypothesis refers to the number of members and the number of academic clubs
if members_hypothesis <= members_premise:
    # check if the estimate of'members_hypothesis' contradicts the number of members reported in the premise
    label = "contradiction"
elif academic_clubs_hypothesis!= academic_clubs_premise:
    # check if the number of academic clubs in the hypothesis contradicts the number of academic clubs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
