****El código consiste en un número entero de 5 dígitos****

 El cual permite calcular el total a pagar además de conocer el tipo de 
paciente, el procedimiento a realizar, su costo y el descuento (o 
recargo) a que tenga derecho. **

• El primer dígito (de izquierda a derecha) indica sí es afiliado (1) o 
particular (2). 
• El segundo dígito determina el servicio que solicita el paciente y 
su costo, sungun costos ya declarados.

La suma del tercero, cuarto y quinto dígito determinara el descuento 
o recargo que se aplicara al paciente, así: 
• Sí la suma es par y el paciente es afiliado tendrá un descuento 
del 15% 
• Sí la suma es par y el paciente es particular tendrá un recargo 
del 15% 
• Sí la suma es impar y el paciente es afiliado tendrá un descuento 
del 25% 
• Sí la suma es impar y el paciente es particular tendrá un recargo 
2 
del 25% 

****Funciones a implementar****: 

• Función validar: Recibe como parámetro un número entero, 
retorna 1 sí el número tiene 5 dígitos, en caso de no cumplir 
retorna 0, para indicar que no es válido. 

• Función tipo: Recibe como parámetro un número entero, sí el 
primer dígito es 1 retorna "AFILIADO", pero sí es 2 retorna 
"PARTICULAR", dato de tipo string. 

• Función servicio: Recibe como parámetro un número entero, el 
segundo dígito permite retornar el nombre del procedimiento a 
realizar. Ejemplo: sí el dígito es 3 retorna "LABORATORIO". 

• Función costo: Recibe como parámetro un dato de tipo string 
con el nombre del servicio a realizar, con base a este se 
determinar el costo base. Ejemplo: sí recibe "LABORATORIO" se 
retorna 25000. 

• Función descuReca: Recibe como parámetro un número entero 
(el código), un dato de tipo string con el tipo de paciente y un 
dato de tipo entero con el costo del procedimiento, y calcula el 
valor del descuento o recargo. 

• Función pago: Recibe como parámetro un número entero 
correspondiente al costo base del servicio y un número float 
correspondiente al descuento o recargo que se aplicara, la 
función retorna el valor final a pagar por el servicio. 

• Función principal: Captura el código del paciente, verifica su 
validez y determina los datos del paciente, haciendo el llamado 
a las diferentes funciones para mostrar en pantalla el costo final 
del servicio. 
