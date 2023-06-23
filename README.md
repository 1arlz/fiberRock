# FiberRock
Word lists and dictionaries for burte force attacks

# Some information...

## DNI

El Documento Nacional de Identidad (DNI) en Argentina tiene un número identificatorio impreso en el frente del documento. Este número es único para cada ciudadano argentino y los extranjeros con residencia permanente en el país. El número de DNI se utiliza para identificar de manera individual a cada persona en los registros y trámites administrativos.

Anteriormente, el número de DNI estaba vinculado a la libreta de enrolamiento (LE) para hombres y la libreta cívica (LC) para mujeres, que eran documentos previos al DNI. Con la implementación del nuevo sistema de DNI, todos los ciudadanos recibieron un nuevo número de identificación.

El número de DNI consta de una secuencia numérica única que puede tener entre 6 y 8 dígitos, dependiendo de la generación del documento. A medida que se emitieron nuevas generaciones de DNI, se introdujeron cambios en la estructura y longitud del número de identificación.

Es importante tener en cuenta que el número de DNI es utilizado ampliamente en diferentes ámbitos, como trámites legales, inscripción en el padrón electoral, acceso a servicios públicos y privados, entre otros. También se utiliza como referencia para establecer la identidad de una persona en diversas situaciones.

## CUIT

El número de CUIT (Clave Única de Identificación Tributaria) en Argentina consta de un total de once (11) cifras y se conforma de la siguiente manera:

Dos dígitos iniciales: Indican el tipo global. Los tipos posibles son:
20, 23, 24, 25, 26 y 27 para personas físicas.
30, 33 y 34 para personas jurídicas (empresas).
Ocho dígitos siguientes: En el caso de personas físicas, corresponden al número de Documento Nacional de Identidad (DNI). En el caso de empresas, es un número de sociedad asignado por la AFIP (Administración Federal de Ingresos Públicos).

Un dígito verificador: Se utiliza para validar la precisión del número de CUIT. El dígito verificador se calcula utilizando el algoritmo Módulo 11. Se toma el número de 10 dígitos compuesto por los 2 primeros dígitos del CUIT y los 8 dígitos siguientes, de derecha a izquierda. Cada dígito se multiplica por los números que componen la serie numérica 2, 3, 4, 5, 6, 7. Luego se suman los resultados de estas multiplicaciones. A este número obtenido se le aplica el módulo 11 (se divide por 11) y se determina el resto de la división. El dígito verificador será la diferencia entre 11 y el resto obtenido. Si el resto es 0, el dígito verificador es 0.

Además, es importante tener en cuenta que para los casos de documentos de 7 dígitos (por ejemplo, DNI), se debe agregar un 0 al inicio del número, de modo que la clave completa tenga el formato: ##-01234567-X.


## CUIL

El número de CUIL (Código Único de Identificación Laboral) en Argentina se conforma de la siguiente manera, de acuerdo con el texto proporcionado:

Prefijo de dos dígitos: El prefijo puede ser 20, 23, 24 o 27. Anteriormente, se utilizaba el prefijo 20 para personas de sexo masculino y 27 para personas de sexo femenino. Sin embargo, a partir de una circular emitida en 2012, el CUIL no se modifica en caso de cambio de género.

Número de DNI: Se utiliza el número de Documento Nacional de Identidad (DNI) de la persona, que consta de ocho dígitos. En caso de que el número de DNI tenga menos de ocho dígitos, se deben completar los espacios restantes con ceros a la izquierda.

Dígito verificador: Es un dígito utilizado para validar la precisión del número de CUIL. Se coloca después del número de DNI y se utiliza para verificar la exactitud de todo el código.

El formato completo del CUIL se expresa de la siguiente manera: "##-########-#" donde ## es el prefijo, ######## es el número de DNI y # es el dígito verificador.


## Dígito verificador

El dígito verificador del CUIL no se calcula utilizando el algoritmo Módulo 11 como en el caso del CUIT. El dígito verificador del CUIL se calcula utilizando el algoritmo conocido como "Módulo 10, base 11".

El proceso para calcular el dígito verificador del CUIL es el siguiente:

Se toma el número de 10 dígitos compuesto por los 2 primeros dígitos del prefijo seguidos de los 8 dígitos del número de DNI, de derecha a izquierda.

Se multiplican estos dígitos por los números que componen la serie numérica 2, 3, 4, 5, 6, 7, 8, 9, 2, 3. Si se han agotado los dígitos de la serie y aún quedan dígitos por multiplicar, se vuelve a comenzar la serie desde el principio.

Se suman los resultados de las multiplicaciones obtenidas en el paso anterior.

Se divide la suma total por 11 y se obtiene el resto de la división.

Si el resto es igual a 0, el dígito verificador es 0. Si el resto es igual a 1, se realiza una regla especial: si el sexo registrado en el CUIL es masculino, el dígito verificador es 9 y si el sexo registrado es femenino, el dígito verificador es 4.

En caso contrario, el dígito verificador es igual a la diferencia entre 11 y el resto obtenido en el paso 4.

Es importante tener en cuenta que el cálculo del dígito verificador del CUIL es específico para el CUIL y no se aplica al cálculo del dígito verificador del CUIT.

## Posibles errores


Si el dígito verificador calculado mediante el algoritmo Módulo 11 no coincide con el dígito verificador real de tu CUIL, puede haber diferentes razones por las que esto ocurra:

Error en la carga de los datos: Es posible que haya ocurrido un error al ingresar o transcribir los números de tu CUIL. Un dígito incorrecto en el número de DNI o en el prefijo puede llevar a un cálculo incorrecto del dígito verificador.

Variaciones en el algoritmo: Aunque el algoritmo Módulo 11 es ampliamente utilizado para calcular el dígito verificador de los números de identificación, puede haber variaciones o excepciones específicas en ciertos casos. Estas variaciones podrían deberse a actualizaciones o particularidades en la normativa aplicada por la entidad encargada de asignar los números de identificación.

Error en la asignación del número: Es posible que haya ocurrido un error en la asignación del CUIL por parte de la entidad responsable, en este caso la Administración Nacional de la Seguridad Social (ANSeS). Esto podría deberse a errores administrativos o fallos en el proceso de asignación de los números de identificación.

En este tipo de situaciones, te recomendaría verificar nuevamente los datos ingresados y, si persiste la discrepancia entre el dígito verificador calculado y el dígito verificador real de tu CUIL, te aconsejo que te comuniques con la ANSeS u otra entidad competente para solicitar aclaraciones y asistencia en la corrección del número de identificación.
