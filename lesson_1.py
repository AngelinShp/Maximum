#N=4, M=5, ИТОГО: 20 повторений
#Сложность: O(N*M)
def strcounter(stroka):
    for symb in set(stroka): #4 значения - значит - 4 повторения
        counter=0
        for sub_symb in stroka: #5 значений в stroka - 5 повт.
            if symb==sub_symb:
                counter+=1
        print(symb, counter)
#Переделаем в Сложность: O(N)
def strcounter_new(stroka):
    syms_counter={}
    for symb in stroka:
        syms_counter[symb]=syms_counter.get(symb, 0)+1
    print(syms_counter)

stroka='aabcd'
print(set(stroka))
strcounter(stroka)

strcounter_new(stroka)