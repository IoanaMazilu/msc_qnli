# Premise: The Bluefin has slowly scoured 95% of the ocean floor that searchers had narrowed down for it.
# Hypothesis: Submersible has combed 95% of a search area with no significant results.
# Golden Label: neutral

search_area_premise = 0.95
search_area_hypothesis = 0.95

# the hypothesis mentions that a submersible has covered 95% of a search area, which is also mentioned in the premise
if search_area_hypothesis != search_area_premise:
    # check if the coverage of the search area in the hypothesis contradicts the coverage reported in the premise
    label = "contradiction"
else:
    # if the coverage in the hypothesis does not contradict the coverage in the premise, we can infer entailment
    label = "entailment"

print(label)

