crayons_paul_birthday = 479.0
crayons_paul_end_year = 134.0
crayons_lost_given = 345.0

# the hypothesis refers to the number of crayons lost or given away
# compute the total number of crayons left after the birthday and the end of the year
total_crayons_left = crayons_paul_birthday - crayons_lost_given
if total_crayons_left!= crayons_paul_end_year:
    # check if the number of crayons left after the birthday and the end of the year is equal to the number of crayons left in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates are consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
