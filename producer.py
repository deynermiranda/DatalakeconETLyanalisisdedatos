import boto3
import json
import time
import pandas as pd
import sys
import os

# --- CONFIGURACIÓN ---
# Definimos el nombre del archivo en una variable constante
NOMBRE_ARCHIVO_CSV = 'iot_telemetry_data.csv'

# Nombre del Stream en AWS
NOMBRE_STREAM = 'iot-sensor-stream'
REGION = 'us-east-1'

# Inicializar cliente de AWS Kinesis
try:
    kinesis = boto3.client('kinesis', region_name=REGION)
except Exception as e:
    print("❌ Error crítico: No se puede conectar con AWS.")
    print("¿Ejecutaste 'aws configure' en tu terminal?")
    print(f"Detalle: {e}")
    sys.exit(1)

def enviar_datos():
    print(f"📂 Buscando archivo: {NOMBRE_ARCHIVO_CSV}...")
    
    # Verificamos si el archivo existe antes de intentar leerlo
    if not os.path.exists(NOMBRE_ARCHIVO_CSV):
        print(f"❌ ERROR: No encuentro el archivo '{NOMBRE_ARCHIVO_CSV}'.")
        print("Asegúrate de que el archivo esté en la carpeta: " + os.getcwd())
        return

    try:
        # Leemos el CSV con Pandas
        df = pd.read_csv(NOMBRE_ARCHIVO_CSV)
        df = df.iloc[56900:] # <--- Saltar las linead ya enviadas

    except Exception as e:
        print(f"❌ Error leyendo el CSV: {e}")
        return

    total_registros = len(df)
    print(f"🚀 Iniciando transmisión de {total_registros} registros a AWS Kinesis...")
    print("💡 Presiona CTRL+C si deseas detenerlo antes.\n")

    # Iterar sobre cada fila del CSV
    for index, row in df.iterrows():
        try:
            # Convertir la fila de Pandas a un diccionario Python normal
            registro = row.to_dict()
            
            # Kinesis necesita Bytes, así que convertimos el diccionario a JSON (texto)
            datos_json = json.dumps(registro)
            
            # Enviar el registro a la nube
            kinesis.put_record(
                StreamName=NOMBRE_STREAM,
                Data=datos_json,
                # Usamos 'device' para ordenar los datos, si no existe usa 'default'
                PartitionKey=str(registro.get('device', 'default')) 
            )
            
            # Feedback visual en la terminal
            print(f"✅ [{index+1}/{total_registros}] Enviado -> Device: {registro.get('device')} | Temp: {registro.get('temp')}")

            # ⏱️ VELOCIDAD DE ENVÍO
            # 0.1 segundos entre envíos (puedes cambiarlo a 0.01 para ir más rápido)
            time.sleep(0.01) 
            
        except KeyboardInterrupt:
            print("\n🛑 Envío detenido por el usuario.")
            break
        except Exception as e:
            print(f"⚠️ Error enviando fila {index}: {e}")

    print("\n🏁 --- Transmisión finalizada ---")

if __name__ == '__main__':
    enviar_datos()
