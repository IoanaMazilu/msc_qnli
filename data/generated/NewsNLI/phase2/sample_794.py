# Premise: Four other workers were still trapped underground in the mine shaft, the Xinhua news agency said.
# Hypothesis: Four miners still trapped underground, state media reported.
# Golden Label: neutral

trapped_workers_premise = 4
trapped_workers_hypothesis = 4

# the hypothesis mentions the number of workers trapped in a mine, which is also referenced in the premise
if trapped_workers_hypothesis != trapped_workers_premise:
    # check if the number of trapped workers in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of trapped workers in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

