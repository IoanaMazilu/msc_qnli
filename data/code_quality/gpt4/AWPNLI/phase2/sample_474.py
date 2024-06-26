red_orchids_premise_vase = 9.0
cut_red_orchids_premise = 15.0
red_orchids_hypothesis = 24.0

# the hypothesis talks about the number of red orchids, which are also referenced in the premise
# find the total number of red orchids in the vase after Sally cut some from her flower garden
total_red_orchids_premise = red_orchids_premise_vase + cut_red_orchids_premise
if red_orchids_hypothesis != total_red_orchids_premise:
    # check if the number of red orchids in the hypothesis contradicts the number of red orchids in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
