# Premise: Mary can type 5 pages in 10 minutes.
# Hypothesis: Mary can type 3 pages in 10 minutes.
# Golden Label: contradiction

pages_premise = 5
pages_hypothesis = 3
time_premise = 10
time_hypothesis = 10

# the hypothesis refers to the number of pages Mary can type in a set amount of time, also mentioned in the premise
if pages_hypothesis > pages_premise and time_hypothesis == time_premise:
    # check if the number of pages in the hypothesis contradicts the number of pages in the premise, given the same amount of time
    label = "contradiction"
elif pages_hypothesis < pages_premise and time_hypothesis == time_premise:
    # if the hypothesis states a lower number of pages for the same amount of time, it can be inferred from the premise
    label = "entailment"
else:
    # if none of the above conditions are met, the relation is neutral
    label = "neutral"

print(label)

