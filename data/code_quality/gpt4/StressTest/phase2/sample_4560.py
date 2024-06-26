pages_premise = 5
pages_hypothesis = 6

# the hypothesis refers to the number of pages Mary can type in 10 minutes
if pages_premise >= pages_hypothesis:
    # check if the number of pages in the premise contradicts the hypothesis of less than 'pages_hypothesis'
    label = "contradiction"
elif pages_premise < pages_hypothesis:
    # if the number of pages in the premise is less than the 'pages_hypothesis', we can infer entailment
    label = "entailment"

print(label)
