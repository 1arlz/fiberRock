# FiberRock
## Word lists and dictionaries for burte force attacks

# Fibertel Argentina

The purpose of this project/script is to demonstrate a Python script that generates dictionaries to crack WPA2 passwords for a specific Internet Service Provider (IPS) in Argentina called Fibertel. Fibertel possesses a common vulnerability that allows for the easy cracking of WiFi passwords.

The vulnerability lies in the default password assignment process during the installation of a new Fibertel WiFi service. By default, Fibertel assigns a password consisting of 10/11 numbers. This password not only corresponds to the customer number displayed on any invoice but also shares a significant portion with the account holder's identification card (DNI).

Exploiting this vulnerability becomes relatively easy for an attacker who has access to the invoice. By simply reading the header, the attacker can obtain the customer number, and consequently, the WiFi password. Even if the invoice is unavailable, there exist multiple methods to obtain a person's identification card number.using just their name and surname, such as websites like www.dateas.com. Additionally, it is widely known that Fibertel's customer numbers for individuals typically start with the digits 004, 014, or 044.

The same vulnerability can be found in the connections of services for businesses.

The only difference is that, in the case of these types of connections, the password usually starts with "010", and the remaining digits represent the beginning of the company's CUIT number (tax identification number).

By incorporating this additional information into our Python script, we can expand its capabilities to crack passwords for both residential and business connections offered by these telecommunications service providers.

In this project, I have developed a Python script that automates the process of generating dictionaries containing the potential passwords based on Fibertel's password assignment patterns. By utilizing these dictionaries in conjunction with password-cracking tools, the potential security risks associated with Fibertel's default password are high. 
The project aims to shed light on the potential risks and vulnerabilities associated with default password practices in both the residential and business sectors.

## DNI

The National Identity Document (Documento Nacional de Identidad or DNI) in Argentina has an identification number printed on the front of the document. This number is unique to each Argentine citizen and foreign residents with permanent residency in the country. The DNI number is used to individually identify each person in records and administrative procedures.

The DNI number consists of a unique numerical sequence that can have between 6 and 8 digits, depending on the generation of the document. As new generations of the DNI were issued, changes were made to the structure and length of the identification number.

## CUIT

The CUIT number (Clave Única de Identificación Tributaria) in Argentina consists of a total of eleven (11) digits and is structured as follows:

- Two initial digits:
  Indicate the global type. The possible types are:
  
  - 20, 23, 24, 25, 26, and 27 for individuals.
  - 30, 33, and 34 for legal entities (companies).

- Eight subsequent digits: In the case of individuals, they correspond to the National Identity Document (Documento Nacional de Identidad or DNI) number. For companies, it is a society number assigned by the AFIP (Administración Federal de Ingresos Públicos).

- One verification digit: It is used to validate the accuracy of the CUIT number. 

The verification digit is calculated using the Module 11 algorithm. The 10-digit number composed of the first two digits of the CUIT and the following eight digits, from right to left, is taken. Each digit is multiplied by the numbers in the numerical series 2, 3, 4, 5, 6, 7. The results of these multiplications are then summed. This obtained number is subjected to module 11 (divided by 11), and the remainder of the division is determined. The verification digit is the difference between 11 and the obtained remainder. If the remainder is 0, the verification digit is 0.

Additionally, it is important to note that in cases of documents with 7 digits (e.g., DNI), a leading 0 must be added to the number so that the complete key has the format: ##-01234567-X


## CUIL

The CUIL number (Código Único de Identificación Laboral) in Argentina is structured as follows, according to the provided text:

- Two-digit prefix: The prefix can be 20, 23, 24, or 27. Previously, the prefix 20 was used for males, and 27 for females. However, since a circular issued in 2012, the CUIL is not changed in case of gender change.

- DNI number: The person's National Identity Document (Documento Nacional de Identidad or DNI) number is used, which consists of eight digits. If the DNI number has fewer than eight digits, the remaining spaces must be filled with leading zeros.

- Verification digit: It is a digit used to validate the accuracy of the CUIL number. It is placed after the DNI number and is used to verify the accuracy of the entire code.

The complete format of the CUIL is expressed as follows: "##-12345678-x" where ## is the prefix, 12345678 is the DNI number, and x is the verification digit.


## Verification digit

The verification digit of the CUIL is not calculated using the Module 11 algorithm like in the case of the CUIT. The verification digit of the CUIL is calculated using the algorithm known as "Module 10, base 11."

The process to calculate the verification digit of the CUIL is as follows:

Take the 10-digit number composed of the first two digits of the prefix followed by the 8 digits of the DNI number, from right to left.

Multiply these digits by the numbers in the numerical series 2, 3, 4, 5, 6, 7, 8, 9, 2, 3. If all the digits in the series have been used and there are still digits left to multiply, restart the series from the beginning.

Sum the results of the multiplications obtained in the previous step.

Divide the total sum by 11 and obtain the remainder of the division.

If the remainder is equal to 0, the verification digit is 0. If the remainder is equal to 1, a special rule is applied: if the registered gender in the CUIL is male, the verification digit is 9, and if the registered gender is female, the verification digit is 4.

Otherwise, the verification digit is equal to the difference between 11 and the remainder obtained in step 4.

It is important to note that the calculation of the verification digit for the CUIL is specific to the CUIL and does not apply to the calculation of the verification digit for the CUIT.

## Common variations and errors


If the verification digit calculated using the Module 11 algorithm does not match the actual verification digit of your CUIL, there may be different reasons why this occurs:

- Data entry error: It is possible that an error occurred when entering or transcribing the numbers of your CUIL. An incorrect digit in the DNI number or the prefix can lead to an incorrect calculation of the verification digit.

- Variations in the algorithm: Although the Module 11 algorithm is widely used to calculate the verification digit of identification numbers, there may be specific variations or exceptions in certain cases. These variations could be due to updates or specific regulations applied by the entity responsible for assigning identification numbers.

- Error in the number assignment: It is possible that an error occurred in the assignment of the CUIL by the responsible entity, in this case, the National Social Security Administration (ANSeS). This could be due to administrative errors or failures in the process of assigning identification numbers.

In these types of situations, is adviced to verifying the entered data again, and if the discrepancy between the calculated verification digit and the actual verification digit of your CUIL persists, you can contact ANSeS or another competent entity to request clarification and assistance in correcting the identification number.

# References
https://medium.com/@closerluc/la-vulnerabilidad-de-las-conexiones-wifi-de-fibertel-argentina-5ea5c9c503b5

https://www.reddit.com/r/argentina/comments/f3bola/psa_si_tienen_fibertel_y_no_cambiaron_la_wifi_la/

https://maurobernal.com.ar/cuil/calcular-el-cuil/


