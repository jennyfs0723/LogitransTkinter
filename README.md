# LOGITRANS - Sistema de Gestión de Distribución (v1)

Este proyecto implementa un prototipo funcional de interfaz gráfica de usuario diseñado en **Python** utilizando **Tkinter**. Su propósito es servir como el "centro de control" digital para la empresa de transporte logístico y distribución *Logitrans*


## Arquitectura del Código
Siguiendo los principios de desarrollo de software y estándares de calidad, el sistema unifica la operación en una ventana centralizada mediante componentes y pestañas independientes encapsulados en 5 clases clave:

1. **`ConfigSistema` (Módulo de Configuración):** Gestión de constantes, versión y en la parte superior tenemos datos de auditoría de la sesión de trabajo (quien, en que version, la fecha y la empresa).
2. **`ModuloCliente` (Módulo Comercial):** Formularioel registro de clientes naturales y empresariales con datos que ayudan a verificar la legitimidad del usuario.
3. **`ModuloEnvios` (Módulo Operativo):** Formulario para la emisión de guías de distribución, control de destinos y pesaje de mercancía.
4. **`ModuloFlota` (Módulo de Transporte):** sistema para el control de envios, saber el conductor y el camion en que estan(en ruta, descanso...)
5. **`ModuloIncidentes` (Módulo de Contingencias):** Línea para reportar novedades viales con descripción del suceso y envío de coordenadas GPS con el fin de saber la ubicacion exacta.

*Tal como lo solicita el trabajo, en esta fase el sistema opera sin datos, simulando la interacción mediante capturas de eventos visuales.*

---

## Requisitos e Instalación
como es un sistema sin dependencias dado que son modulos nativos de python no requiere instalaciones externas diferentes a pycharm.

1. tener instalada la version mas reciente de pycharm.
2. Descargar o clonar este repositorio en el computador de uso.
3. Abre el archivo main.py y ponlo a correr.
* El archivo solo se ejecutara en la carpeta main dado que es la instruccion final que se le dio al sistema mediante el codigo if __name__ == '__main__': *

---

## Simulación de Respuestas y Calidad (UI/UX)
Cada formulario cuenta con un botón operativo que gatilla eventos gráficos controlados a través de la librería `messagebox`, variando su comportamiento según la gravedad o urgencia de la acción:
* **Información Exitosa (`showinfo`):** Utilizado al guardar clientes y generar guías de envío para confirmar que los datos cumplen los estándares de la interfaz.
* **Advertencia Preventiva (`showwarning`):** se ejecuta cuando obtenemos la info del vehiculo
* **Alerta Crítica (`showerror`):** Activado en la sección de incidentes para notificar eventos viales en ruta al centro de distribución de manera inmediata.
