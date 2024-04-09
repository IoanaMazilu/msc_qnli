drawer_pencils_premise = 43.0
desk_pencils_premise = 19.0
additional_pencils_premise = 16.0
total_pencils_hypothesis = 81.0

# compute the total number of pencils in the premise
total_pencils_premise = drawer_pencils_premise + desk_pencils_premise + additional_pencils_premise

if total_pencils_hypothesis > total_pencils_premise:
    # the hypothesis implies more pencils than the premise, so we have entailment
    label = "entailment"
elif total_pencils_hypothesis < total_pencils_premise:
    # the hypothesis implies fewer pencils than the premise, so we have contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
