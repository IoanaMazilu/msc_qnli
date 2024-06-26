books_bargin_premise = 41.0
books_off_bin_premise = 2.0
books_sold_premise = 33.0
books_bin_hypothesis = 3.0

# the hypothesis refers to the number of books in the bargin bin, which are also mentioned in the premise
# compute the number of books in the bargin bin in the premise
books_bin_premise = books_bargin_premise - books_off_bin_premise
if books_bin_hypothesis!= books_bin_premise:
    # check if the number of books in the bin in the hypothesis contradicts the number of books in the bin from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
