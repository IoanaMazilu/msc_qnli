photos_taken_by_octavia_premise = 36
photos_taken_by_octavia_hypothesis = 66

# the hypothesis refers to the number of photos taken by Octavia, also mentioned in the premise
if photos_taken_by_octavia_hypothesis != photos_taken_by_octavia_premise:
    # check if the number of photos taken by Octavia in the hypothesis contradicts the number of photos taken by Octavia in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
