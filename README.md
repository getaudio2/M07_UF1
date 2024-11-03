# ACTIVITAT 7 - PYTHON + POSTGRESQL

## CREATE
La funció `create_user()` rep les dades introduïdes per l'usuari. Aquestes son emmagatzemades en variables per executar-les dins de la query insert amb `connection.execute(query, values)`.
![captura](/ACTIVITAT7/captures/cap1.png)
Amb postgres podem comprovar que l'usuari John Doe s'ha creat correctament.
![captura](/ACTIVITAT7/captures/cap2.png)
## READ
Aquesta vegada la funció executa un select i agafa les files retornades de la BBDD amb `connection.fetchall()`.
![captura](/ACTIVITAT7/captures/cap3.png)  
Podem comprovar que funciona, i ens retorna un array amb les files d'usuaris.
![captura](/ACTIVITAT7/captures/cap4.png)
## UPDATE
Similar amb la funció `create_user()`, però aquest cop amb l'id de l'usuari a modificar.
![captura](/ACTIVITAT7/captures/cap5.png)
Aqui l'usuari introdueix per terminal les dades a modificar de l'usuari.  
![captura](/ACTIVITAT7/captures/cap6.png)
Comprovem els canvis a postgres.
![captura](/ACTIVITAT7/captures/cap7.png)
## DELETE
![captura](/ACTIVITAT7/captures/cap8.png)  
Pasem per terminal l'id de l'usuari que volem esborrar.  
![captura](/ACTIVITAT7/captures/cap9.png)  
Comprovem que l'usuari s'hagi eliminat amb postgres.  
![captura](/ACTIVITAT7/captures/cap10.png)
