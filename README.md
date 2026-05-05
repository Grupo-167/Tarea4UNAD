## **Tarea4UNAD**
Tarea #4 de Programacion — Curso: Programación 213023 | UNAD  
Programa: Ingeniería de Sistemas | Escuela ECBTI

Bitacora de Avances del maneo de errores y pruebas del software (Roussell Nova)


### [v0.1] Primera Interevencion 

Se realizo la primera simulacion de los logs, se realizo el 04/05/2026, evidenciandose en el archivo .log sus respectivos avances, estas pruebas validan que funcionan correctamente los logs de crear, eliminar, ver y las excepciones intencionales realizadas para las pruebas

`excepciones.py`
Se creo una jerarquía completa de excepciones personalizadas partiendo de la clase base "ErrorSistemaF". Se crearon diez excepciones específicas:
-nombres vacios
-error de edad invalida
-error de estado invalido
-error de cliente no encontrado en la bd
-error de servicios no disponibles
-error de duracion invalida
-error de recerva incorrecta
-error de vancelacion de reerva
-error de capo faltantes para realizar submit de los datos
-error de tipo incorrecto

`logger.py`
Se implementó el sistema centralizado de registro de eventos utilizando el módulo logging.py de Python. Todos los errores, advertencias y eventos relevantes del sistema quedan almacenados automáticamente en el archivo sistema_fj.log, el cual se sobre escribe para guardar nuevos logs y se encuentra en la carpeta raiz del proyecto

Por el momento se pensaron en 4 logs
-log de eventos
-log de errores
-log de advertencias
-log critico

los cuales me encargue de exportar a cada una de los archivos de mi compañeros

`simulacion.py`
archivo de monitoreo de errores( NO TOCAR )
doce operaciones simuladas que demuestran el comportamiento del sistema ante datos válidos e inválidos

este archivo se creo para generar un log que registre cada cambio realizado por la rama de logs y errores, la idea es eecutar uno cada commit y que quede la trazabilidad de futuros errores a revisar y en que cambio especifico dejaron de funcionar


- ## **Archivos modificados** -

 03/05/2026 se modifico "clientes" y se reemplazaron los valueerrors de los setters para sincronizarlo con el archivo de escepciones y en los CRUDS del mismo se incorporaronm bloques try/except/else/finally asi como la incorpóracioin del sistema de auditoria de errores, asi como tambien se arreglaron algunos detalles que interferian para que el codigo funcionara mas limpiaente

04/05/2026 se modifico el archivo "main" para integrar los modulos "logger" y "simulacion" en el menu, asi como un pequeño cambio en la execucion del mismo en forma de prevencion de errores al principio de la aplicacion, se solucionaron redundancias
