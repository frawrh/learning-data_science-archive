"""
Implement clean_names(names). The function receives a list of participant names. For every name: (1) remove whitespace from the beginning and end, (2) replace repeated spaces between words with a single space, (3) convert the name to title case, and (4) preserve the original ordering. Return the cleaned list.

Example 1: Input: [" aLYA putri ", "BUDI", "citra lestari"] Output: ["Alya Putri", "Budi", "Citra Lestari"]
Example 2: Input: [" muhammad rizky ", "SINTA"] Output: ["Muhammad Rizky", "Sinta"]

Input Format
This is a function-based challenge. The parameter names is a list of strings.

Constraints
1 <= len(names) <= 10^4. Names may contain leading, trailing, or repeated whitespace.

Output Format
Return a list of cleaned name strings in the same order as the input.

Sample Input 0
3
  aLYA putri 
BUDI
citra   lestari

Sample Output 0
Alya Putri
Budi
Citra Lestari
"""


def clean_names(names):
    bersih = []
    for name in names:
        sudah = " ".join(name.split()).title()
        bersih.append(sudah)
    return bersih
    
if __name__ == '__main__':
    masukan = int(input())
    names = []
    for _ in range(masukan):
        names.append(input())
        
    hasil = clean_names(names)
    
    for nama in hasil:
        print(nama)
