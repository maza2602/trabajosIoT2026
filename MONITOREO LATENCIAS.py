#  trabajar con lista fija, 5 direcciones ip
#  monitoreo continuo, 24/7 en tiempo real
#  escaneo de inventario ordenado, revisar 1 listo, revisar 2 listo, ...
#  toma de decisiones, logica de los estados
#  para cada ip el sistema debe simular un estado de red aleatorio, debe mostrar 3 estados; if exitoso con latencia normal,
#  elif si la conexion es exitosa pero con latencia alta, else si falla la conexion
#  el script debe ser visual 
#  realismo de output, los mensajes en pantalla deben usar colores de alerta: rojo, amarillo y verde

# libreria time para espera entre ciclos de monitoreo
import time
# se importa libreria para numeros aleatorios
import random as rnd
# se importa colorama para pintar los textos rojo, amarillo y verde
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# definiendo lista de ips
direcciones = ["13.114.140.27", "85.177.110.151", "94.230.3.103", "45.208.175.164", "203.25.107.73"]

# funcion que define latencias aleatorias
def latenciarnd():
    return rnd.uniform(1.0, 300.0)

def monitoreo_continuo():
    print(Style.BRIGHT + "----INICIANDO MONITOREO EN TIEMPO REAL----\n")
    ciclo = 1
    
    while True:
        print(f"\n--- Escaneo de inventario ordenado - Ciclo #{ciclo} ---")
        
        for i, ip in enumerate(direcciones, start=1):
            latencia = latenciarnd()
            
            # latencia normal menos de 100 ms -> VERDE
            if latencia < 100.0:
                print(f"Revisar {i} listo: {Fore.GREEN} [ACTIVO] {ip:<15} -> Latencia Normal: {latencia:.1f} ms - Paquetes: enviados = 4, recibidos = 4, perdidos = 0 - Tiempos aproximados de ida y vuelta en milisegundos: Mínimo = {rnd.randint(0, 3)}ms, Máximo = {rnd.randint(0, 3)}ms, Media = {rnd.randint(0, 3)}ms")
            
            # latencia alta entre 100 ms y 250 ms -> AMARILLO
            elif latencia <= 250.0:
                print(f"Revisar {i} listo: {Fore.YELLOW} [ALERTA] {ip:<15} -> Latencia Alta:   {latencia:.1f} ms - Paquetes: enviados = 4, recibidos = 3, perdidos = 1 - Tiempos aproximados de ida y vuelta en milisegundos: Mínimo = {rnd.randint(4, 7)}ms, Máximo = {rnd.randint(4, 7)}ms, Media = {rnd.randint(4, 7)}ms")
            
            # falla por latencia extrema mss de 250 ms -> ROJO
            else:
                print(f"Revisar {i} listo: {Fore.RED} [FALLO] {ip:<15} -> Falla por lentitud: {latencia:.1f} ms - Tiempo de espera agotado para esta solicitud")
                
            time.sleep(0.4)
            
        print("-" * 65)
        ciclo += 1
        time.sleep(5)

if 1 > 0:
    try:
        monitoreo_continuo()
    except KeyboardInterrupt:
        print(Style.BRIGHT + f"\n{Fore.CYAN}Monitoreo detenido por el usuario.")
