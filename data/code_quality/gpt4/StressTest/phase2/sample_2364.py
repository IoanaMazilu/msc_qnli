iphone_users_premise = 40
iphone_users_hypothesis = 50
bmw_owners_premise = 12
bmw_owners_hypothesis = 12
boys_premise = 70
boys_hypothesis = 70

# the hypothesis refers to the percentages of employees using iPhone, owning a BMW car and being boys mentioned in the premise
if iphone_users_hypothesis <= iphone_users_premise:
    # check if the estimate of 'iphone_users_hypothesis' contradicts the percentage of iPhone users in the premise
    label = "contradiction"
elif bmw_owners_hypothesis != bmw_owners_premise:
    # check if the percentage of BMW owners in the hypothesis contradicts the percentage of BMW owners reported in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the percentage of boys in the hypothesis contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
