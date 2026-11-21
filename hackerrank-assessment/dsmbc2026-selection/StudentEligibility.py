"""
Implement qualified_students(records). Each record has the format name|score|attendance. A student qualifies when score >= 70 and attendance >= 80. Both score and attendance must be valid integers. Ignore malformed records: records without exactly three fields, non-integer scores, or non-integer attendance. Return qualified names sorted alphabetically.

Example: Input: ["Alya|82|90", "Budi|65|95", "Citra|75|82", "Doni|80|60", "Eka|abc|90"] Output: ["Alya", "Citra"]

Input Format
The first line contains n. Each of the next n lines contains one record in the format name|score|attendance.

Constraints
1 <= n <= 10^4. Names do not contain the | character.

Output Format
Print each qualified student name on its own line in alphabetical order.

Sample Input 0
5
Alya|82|90
Budi|65|95
Citra|75|82
Doni|80|60
Eka|abc|90

Sample Output 0
Alya
Citra
"""


def qualified_students(records):
    qualified = []
    for record in records:
        pisah = record.split('|')
        if len(pisah) != 3:
            continue
            
        try:
            score = int(pisah[1])
            attendance = int(pisah[2])
        except ValueError:
            continue
            
        if score >= 70 and attendance >= 80:
            nama = pisah[0]
            qualified.append(nama)
            
    qualified.sort()
    return qualified
    

if __name__ == '__main__':
    jumlahMasukan = int(input())
    records = []
    for _ in range(jumlahMasukan):
        records.append(input())
        
    hasil = qualified_students(records)
    
    for eligible in hasil:
        print(eligible)
