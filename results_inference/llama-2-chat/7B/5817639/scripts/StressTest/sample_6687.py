book_purchased_premise = 60
book_purchased_hypothesis = 40

# the hypothesis talks about the number of books purchased by Bookman, which is also mentioned in the premise
if book_purchased_hypothesis <= book_purchased_premise:
    # check if the hypothesis value contradicts the estimate of 'book_purchased_premise'
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise:
    # check if the number of hardback copies in the hypothesis contradicts the number of hardback copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
