#Escreva programa que leia um valor em metros e o exiba convertido em centimetros e milímetros
print("\033[1;94;46m"+"="*35+"\033[0;0m")
m = float(input("\033[1;96m"+'Escreva um valor em metros:'))
print("\033[1;94;46m"+"="*35+"\033[0;0m")
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print("\033[1;94m"+f'A medida {m}m corresponde a:\nEm quilômetros é {km}km! \nEm hectômetros é {hm}hm! \nEm decâmetros é {dam}dam! \nEm decímetros é {dm:.0f}dm! \nEm centimetros é {cm:.0f}cm! \nEm milímetros é {mm:.0f}mm!')
print("\033[1;94;46m"+"="*35+"\033[0;0m")
