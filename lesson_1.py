#N=4, M=5, ИТОГО: 20 повторений
#Сложность: O(N*M)
def strcounter(stroka):
    for sym in set(stroka): #4 значения - значит - 4 повторения
        counter=0
        for sub_sym in stroka: #5 значений в stroka - 5 повт.
            if sym==sub_sym:
                counter+=1
        print(sym, counter)
#Переделаем в Сложность: O(N)
def strcounter_new(stroka):
    syms_counter={}
    for sym in stroka:
        syms_counter[sym]=syms_counter.get(sym, 0)+1
    print(syms_counter)

stroka='aabcd'
print(set(stroka))
strcounter(stroka)

strcounter_new(stroka)

#ДЗ:
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('лепсспел'))
#
#dsgdfhd

