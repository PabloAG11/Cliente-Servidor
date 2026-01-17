# Almaguer-Gomez-Juan-Pablo
# Villalpando-Casillas-Luz-Andrea

Tópicos para el Despliegue de Aplicaciones

¨*Presentación:
Comunicación Cliente–Servidor usando Sockets en Python
Este proyecto implementa un sistema básico de comunicación cliente–servidor utilizando el lenguaje de programación Python y el módulo socket, el cual permite el intercambio de información a través de una red local mediante el protocolo TCP/IP.
El sistema está compuesto por dos programas independientes:
Servidor, encargado de escuchar y atender conexiones.
Cliente, encargado de conectarse al servidor y enviar mensajes.
El objetivo principal es demostrar el funcionamiento de una arquitectura cliente–servidor y comprender cómo se establece una comunicación de red a bajo nivel.

*Funcionamiento del Servidor
El servidor se configura para:
Escuchar conexiones en todas las interfaces de red (0.0.0.0).
Utilizar el puerto 8000 para la comunicación.
Aceptar una conexión entrante de un cliente.
Recibir mensajes enviados por el cliente.
Mostrar los mensajes en consola.
Enviar una respuesta confirmando la recepción del mensaje.
El servidor permanece activo hasta que el cliente cierra la conexión.

* Funcionamiento del Cliente
El cliente se configura para:
Conectarse a la dirección IP del servidor.
Utilizar el mismo puerto configurado en el servidor.
Permitir al usuario escribir mensajes desde el teclado.
Enviar los mensajes al servidor.
Recibir y mostrar la respuesta del servidor
El cliente puede finalizar la comunicación escribiendo la palabra “salir”.

Protocolo TCP/IP
En este proyecto se utiliza el protocolo TCP (Transmission Control Protocol), el cual forma parte del modelo TCP/IP, ampliamente usado para la comunicación en redes e Internet.
TCP es un protocolo orientado a conexión, lo que significa que antes de intercambiar datos se debe establecer una conexión segura entre el cliente y el servidor.

Funcionamiento del Protocolo TCP en el Proyecto
El servidor crea un socket TCP y se queda a la espera de conexiones en un puerto específico.
El cliente solicita una conexión al servidor usando su dirección IP y el puerto configurado.
TCP establece la conexión asegurando que ambos extremos estén sincronizados.
Se realiza el intercambio de mensajes entre cliente y servidor.
Cuando el cliente termina, la conexión se cierra de forma ordenada.
