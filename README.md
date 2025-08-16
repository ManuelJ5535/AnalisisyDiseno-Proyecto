
# Proyecto P#2 | Análisis y diseño de sistemas.


Manuel Antonio Jiménez Victor,
Javier Cerdas Reyes,
Lex Rojas Monge.





Universidad Internacional San Isidro Labrador.


Curso:
Análisis y diseño de sistemas.
Código: ISB-23.

Profesor:
Estefanía Boza Villalobos.

Nota del Autor:
El presente trabajo es requisito para optar por la aprobación del curso ANÁLISIS Y DISEÑO DE SISTEMAS, código del curso: ISB-23, del Bachillerato en Ingeniería de Sistemas, en la Universidad Internacional San Isidro Labrador. Para contactar al autor escriba por correo electrónico a: manuel.antonio5535@gmail.com





Introducción.

     Desarrollaremos un sistema de Reservas de cuartos en un hotel, que permita a los usuarios realizar reservas, consultar disponibilidad y gestionar sus reservas de manera sencilla y eficiente.

# Requisitos. 

## Requisitos funcionales:
* Los usuarios podrán registrarse e iniciar sesión en el sistema
* Los usuarios pueden buscar habitaciones disponibles por fecha y tipo de habitación.
* Los usuarios podrán realizar sus reservas, modificarlas o cancelarlas.
* El administrador puede gestionar las habitaciones (añadir, editar o eliminar).
* El sistema debe mostrar un resumen de la reserva y enviar un correo de confirmación.

## Requisitos no funcionales:
* El sistema debe ser responsive (funcionar en dispositivos móviles y de escritorios).
* El tiempo de respuesta del sistema debe ser menor a 2 segundos.
* El sistema debe garantizar la seguridad de los datos de los usuarios (encriptación de contraseñas).
* Debe ser compatible con los navegadores más comunes (Chrome, Firefox y Safari).




# Modelo de ciclo de vida/metodología seleccionada con su justificación. 

## 1. ¿Por qué SCRUM es adecuado para este proyecto?

SCRUM es una metodología ágil ideal para proyectos con requisitos dinámicos, como un sistema de reservas de hotel, debido a:
+ Flexibilidad: Permite adaptarse a cambios en los requisitos (ej.: nuevas políticas de cancelación, integración con APIs de pago no previstas inicialmente).
+ Entregas incrementales: El sistema puede lanzarse por módulos funcionales (ej.: primero reservas básicas, luego gestión de pagos, después panel de admin).
+ Feedback continuo: Los dueños del hotel (stakeholders) pueden probar versiones tempranas y ajustar prioridades.

## 2. Beneficios Clave para el Desarrollo
Sprints cortos (2-4 semanas).  
Permite entregar funcionalidades útiles rápidamente (ej: búsqueda de disponibilidad en el primer sprint).  
Reuniones diarias (Daily Standups)	Ayuda a identificar bloqueos rápidamente (ej.: problemas con la API de pagos).    
Priorización con Backlog  
El Product Owner puede ajustar prioridades según necesidades del negocio (ej.: añadir promociones temporales).  
Transparencia (Scrum Board).  
Todo el equipo ve el progreso (ej.: reservas completadas vs. pendientes de testing).  

## 3. Ejemplo de Aplicación en el Proyecto
Sprint 1: MVP con búsqueda de habitaciones y reserva básica.  
Sprint 2: Integración con pasarela de pagos.  
Sprint 3: Panel de administración y reportes.  
Sprint 4: Funcionalidades avanzadas (cancelaciones flexibles, notificaciones por email).  

## 4. Riesgos Mitigados por SCRUM
Cambios de último momento: Se ajustan en retrospectivas sin retrasar todo el proyecto.  
Falta de alineación: Las revisiones de sprint (Sprint Reviews) aseguran que el cliente valide el trabajo.  
Sobrecarga del equipo: El Sprint Planning define metas realistas por iteración.  

## 5. Alternativas Consideradas 
Cascada: Rígido para un proyecto con requisitos variables.

## 6.Conclusión
SCRUM es la mejor opción porque:
+ Alinea desarrollo con necesidades reales del hotel mediante iteraciones rápidas.
+ Reduce riesgos al validar funcionalidades temprano.
+ Promueve la colaboración entre desarrolladores, administradores y clientes.

# Diseño realizado
## División de tareas por Historias de usuario.
	
La siguiente tabla son las tareas a realizar que quiere el cliente llamado historias de usuario, estás se lograron de una reunión con el cliente que nos específico cada una de las cosas que quiere que haga el proyecto, se le asignaron story points para poder asociarlos a una cantidad de personas (imaginarias) y una cantidad de tiempo (estimada).


| ID  | Historia de Usuario | Story Points | Criterios |
| ------------- | ------------- | ------------- | ------------- |
| P1  | Como usuario quiero registrarme e iniciar sesión para gestionar mis reservas.  | 3 | Contraseña encriptada; validación de email; login devuelve token. |
| P2  | Como usuario quiero buscar habitaciones por fecha y tipo para ver disponibilidad. | 5 | Resultado consistente con DB; muestra cantidad disponible. |
| P3 | Como usuario quiero reservar una habitación para confirmar mi estancia.  | 8 | Bloqueo temporal; reserva en DB; email enviado con resumen. |
| P4  | Como usuario quiero modificar mi reserva para ajustar fechas o tipo.  | 5 | Re-validar disponibilidad; actualizar DB; enviar email de modificación. |
| P5  | Como usuario quiero cancelar mi reserva.  | 3 | Reserva marcada como cancelada; liberar disponibilidad; email enviado. |
| P6 | Cómo admin quiero añadir, editar o eliminar habitaciones.  | 5 | Cambios visibles en búsqueda inmediatamente; registro de cambios. |
| P7  | Como sistema quiero enviar correos de confirmación, modificación y cancelación.  | 2 | Correo enviado dentro de 1 min; contenido con datos correctos. |
| P8  | Optimizar el sistema para tiempos de respuesta menores a 2 segundos. | 5 | Pruebas de rendimiento superadas; carga simulada con >100 usuarios concurrentes. |
| P9 | Garantizar compatibilidad con navegadores Chrome, Firefox y Safari.  | 2 | Pruebas cross-browser aprobadas; UI y funciones estables. |
| P10  | Implementar UI responsive para móviles y escritorio. | 3 | UI adaptable en pruebas; no hay elementos cortados o mal alineados. |
| P11  | Encriptar contraseñas y proteger datos de usuarios. | 5 | Contraseñas con hashing seguro (BCrypt); HTTPS obligatorio. |
| P12  | Configurar sistema de caché para disponibilidad. | 5 | Disponibilidad recuperada  desde cache; fallback a DB si no está en caché. |



# Componentes: 

## Cliente:
+ Web responsive (desktop/mobile) — UI: búsqueda, calendario, formularios de reserva, perfil, panel admin.


## API:
+ Módulo de autenticación: registro, login, JWT/session, encriptación de contraseñas.
+ Módulo de Búsqueda y Disponibilidad: filtros por fecha, tipo de habitación, disponibilidad en tiempo real, caching corto.
+ Módulo de Gestión de Reservas: crear, editar, cancelar, historial de reservas.
+ Módulo Admin de Habitaciones: CRUD de habitaciones (tipos, precios, fotos, inventario).
+ Módulo de Notificaciones/Email: generación de resumen y envío de confirmación (correo).
+ Módulo de Reportes / Logs / Monitorización: tiempos de respuesta, errores, auditoría.
+ Módulo de Seguridad: validaciones, protección contra CSRF, rate limiting, cifrado en tránsito.

##Persistencia:
+ Base de datos relacional.

