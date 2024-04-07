# Premise: Each of the less than 79 members in Mount school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Hypothesis: Each of the 59 members in Mount school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Golden Label: neutral

members_premise = 79
members_hypothesis = 59
min_clubs_premise = 1
max_clubs_premise = 3
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# the hypothesis talks about the number of members in Mount school class and the range of academic clubs they can sign up for, both mentioned also in the premise
if members_hypothesis >= members_premise:
    # check if the number of members in the hypothesis contradicts the premise estimate of less than 'members_premise'
    label = "contradiction"
elif min_clubs_hypothesis != min_clubs_premise or max_clubs_hypothesis != max_clubs_premise:
    # check if the range of academic clubs each member can sign up for contradicts the range specified in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

