members_premise = 59
members_hypothesis = 79
min_clubs_premise = 1
max_clubs_premise = 3
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# The hypothesis talks about the number of members and the clubs they need to sign up for, referenced also in the premise
if members_hypothesis < members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
elif min_clubs_hypothesis != min_clubs_premise or max_clubs_hypothesis != max_clubs_premise:
    # check if the number of clubs in the hypothesis contradicts the number of clubs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we infer entailment here since premise explicitly provides the same membership and club details
    label = "entailment"

print(label)
