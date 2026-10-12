"""
Implement category_frequency(categories). For each category, remove surrounding whitespace and convert it to lowercase. Ignore empty category names. Count occurrences and return strings in the form category=count, sorted alphabetically by category.

Example 1: Input: ["Food", " food ", "Technology", "FOOD", "Books", " technology "] Output: ["books=1", "food=3", "technology=2"]
Example 2: Input: ["A", "B", "a", "C", " b "] Output: ["a=2", "b=2", "c=1"]

Input Format
The first line contains n. Each of the next n lines contains one category name.

Constraints
1 <= n <= 10^4. Category names may contain surrounding whitespace and mixed case.

Output Format
Print one category=count string per line, sorted alphabetically by category.

Sample Input 0
6
Food
 food 
Technology
FOOD
Books
 technology 
 
Sample Output 0
books=1
food=3
technology=2
"""


def category_frequency(categories):
    hitung = {}
    for j in categories:
        bersih = j.strip().lower()
        
        if bersih == "":
            continue
        
        if bersih in hitung:
            hitung[bersih] += 1
        else:
            hitung[bersih] = 1
            
    hasil_list = []
    
    for k in sorted(hitung.keys()):
        hasil_list.append(f"{k}={hitung[k]}")
    
    return hasil_list

if __name__ == '__main__':
    jumlahInput = int(input())
    categories = []
    for _ in range(jumlahInput):
        categories.append(input())
        
    hasil = category_frequency(categories)
    
    for i in hasil:
        print(i)

"""
