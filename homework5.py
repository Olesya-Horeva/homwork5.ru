immutable_var = (1,2,'apple')
print(immutable_var)
#immutable_vat[2]= 'banana'
#print(immutable_var) при попытке изменения элемента кортежа, выводит ошибку, так как кортеж относится к
# неизменяемым спискам.
mutable_list = ['телевизор','компьютер','телефон']
mutable_list[0] = 'магнитофон'
print(mutable_list)

