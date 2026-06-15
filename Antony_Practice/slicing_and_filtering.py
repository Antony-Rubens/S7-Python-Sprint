
#you can use :def process_placement_scores(scores: list[int], L: int, R: int) -> list[int]:
#But it is not necessary to use type hints in python, it is just for better readability and understanding of the code.
def process_placement_scores(score,l,r):
#I am writing score list from l to r as r to l: 
#I used chaining of two slices [l:r+1] and [::-1]
    score[l:r+1] = score[l:r+1][::-1]
#Now I create a new list for looping inside it with some conditions to learn comprehension:
    new_score = [x + 5 for x in score if x > 40 ]
    return score,new_score
# This line passes the integers and lists directly in, bypassing input()
print(process_placement_scores([25, 35, 45, 15, 55, 60, 20], 1, 4))