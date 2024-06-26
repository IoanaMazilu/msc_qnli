 class_books_premise = 54.0
given_books_premise = 23.0
class_books_hypothesis = 34.0

# the hypothesis refers to the number of books left in the class, which is also mentioned in the premise
# compute the number of books left in the class in the premise
class_books_premise_left = class_books_premise - given_books_premise
if class_books_hypothesis!= class_books_premise_left:
    # check if the number of books left in the class in the hypothesis contradicts the number of books left in the class from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
