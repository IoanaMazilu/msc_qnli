# Premise: Mary can type less than 6 pages in 10 minutes.
# Hypothesis: Mary can type 5 pages in 10 minutes.
# Golden Label: neutral

pages_premise = 6
pages_hypothesis = 5

# the hypothesis refers to the number of pages Mary can type in 10 minutes, also mentioned in the premise
if pages_hypothesis >= pages_premise:
    # check if the number of pages in the hypothesis contradicts the premise estimate of less than 'pages_premise'
    label = "contradiction"
elif pages_hypothesis < pages_premise:
    # if the number of pages in the hypothesis is less than the premise estimate, we can infer entailment
    label = "entailment"

print(label)

