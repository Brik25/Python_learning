import operator
import random
a={}

'generate dict'
for type_1 in range(10):
    a[type_1] = random.randint(0,100)

FullDictOperator = {"Acem":dict(sorted(a.items(),key=operator.itemgetter(1))),
                    "Decem":dict(sorted(a.items(),key=operator.itemgetter(1), reverse=True))}

for pos in FullDictOperator:
    Resualt = ""
    for ValueDict in FullDictOperator[pos]:
        Resualt = str(Resualt)  + str(FullDictOperator[pos][ValueDict])+ ","
    print(str(pos) + ":" +Resualt )