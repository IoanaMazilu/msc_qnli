iphone_users_premise = 40
iphone_users_hypothesis = 40
bmw_owners_premise = 12
bmw_owners_hypothesis = 12
boys_premise = 70
boys_hypothesis = 70

# the hypothesis refers to the same percentages of employees using iPhone, owning BMW cars, and being boys, as mentioned in the premise
if iphone_users_hypothesis >= iphone_users_premise:
    # check if the hypothesis statement contradicts the percentage of iPhone users in the premise
    label = "contradiction"
elif bmw_owners_hypothesis != bmw_owners_premise:
    # check if the percentage of BMW owners in the hypothesis contradicts the percentage of BMW owners in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the percentage of boys in the hypothesis contradicts the percentage of boys mentioned in the premise
    label = "contradiction"
else:
    # if none of the hypothesis statements contradicts the premise, we can infer entailment
    label = "entailment"

print(label)
