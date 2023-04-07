#Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.
numberList=[]
for i in range(1,11):
  value=int(input("sayı girin"))
  numberList.append(value)
print("max sayi:", max(numberList))


#Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.
up_limit=int(input("üst limit girin"))
my_list=[]
for i in range(0,up_limit,2):
    my_list.append(i)
print(my_list)



#alt ve üst limitleri kullanıcı tarafından belirlenen ve aradaki çift sayılar gösteren program.

up_limit=int(input("üst limit girin"))
low_limit=int(input("alt limit girin"))
my_list=[]
for i in range(low_limit,up_limit,2):
    if i%2!=0:

     my_list.append(i+1)
    elif i%2==0:
       my_list.append(i)
print(my_list)

