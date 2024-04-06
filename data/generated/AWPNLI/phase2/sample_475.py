# Premise: There were 9.0 red orchids and 3.0 white orchids in the vase and Sally cut 15.0 red orchids from her flower garden and put them in the vase.
# Hypothesis: 27.0 red orchids are there now in the vase.
# Golden Label: contradiction

red_orchids_vase_premise = 9.0
white_orchids_vase_premise = 3.0
cut_red_orchids_premise = 15.0
red_orchids_vase_hypothesis = 27.0

# the hypothesis refers to the number of red orchids in the vase, which are also mentioned in the premise
# compute the total number of red orchids in the vase from the premise
total_red_orchids_vase_premise = red_orchids_vase_premise + cut_red_orchids_premise
if red_orchids_vase_hypothesis != total_red_orchids_vase_premise:
    # check if the number of red orchids in the vase from the hypothesis contradicts the number of red orchids in the vase from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

