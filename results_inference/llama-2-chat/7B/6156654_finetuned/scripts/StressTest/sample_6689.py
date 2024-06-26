copies_purchased_premise = 60
copies_purchased_hypothesis = 60
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
paperback_copies_premise = 50
paperback_copies_hypothesis = 50

# the hypothesis refers to the number of books purchased and their format, which are also mentioned in the premise
if copies_purchased_hypothesis!= copies_purchased_premise:
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise or paperback_copies_hypothesis!= paperback_copies_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
