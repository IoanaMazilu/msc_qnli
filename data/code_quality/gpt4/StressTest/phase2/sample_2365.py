iphone_users_premise = 50
iphone_users_hypothesis = 40
bmw_owners_premise = 12
bmw_owners_hypothesis = 12
boys_premise = 70
boys_hypothesis = 70

# the hypothesis refers to the percentages of employees using iPhone, owning a BMW and being boys, which are also mentioned in the premise
if iphone_users_hypothesis >= iphone_users_premise:
    # check if the percentage of 'iphone_users_hypothesis' contradicts the estimate of less than 'iphone_users_premise'
    label = "contradiction"
elif bmw_owners_hypothesis != bmw_owners_premise or boys_hypothesis != boys_premise:
    # check if the percentages of BMW owners or boys in the hypothesis contradict the corresponding percentages in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
