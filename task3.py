#Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC
a = float(input("Координата точки А на числовой оси: "))
b = float(input("Координата точки В на числовой оси: "))
c = float(input("Координата точки С на числовой оси: "))
while not((a<c<b) or (a>c>b)):
	print("Точка С должна располгагаться между точками А и В.\nВведите координаты заново.")
	a = float(input("Координата точки А на числовой оси: "))
	b = float(input("Координата точки В на числовой оси: "))
	c = float(input("Координата точки С на числовой оси: "))
b = abs(b-a)
c = abs(c-a)
print("Произведение отрезков АС и ВС: "+str(b*c))
