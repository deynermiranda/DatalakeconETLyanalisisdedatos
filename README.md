#  AWS Data Lake: Procesamiento de datos IoT meteorológicos en tiempo real

##  Descripción del Proyecto
Sistema de Data Lake completamente serverless en AWS para ingerir, procesar, transformar (ETL) y analizar datos meteorológicos IoT en tiempo real. Implementa arquitectura de 3 capas (Raw/Processed/Curated).

## Requisitos

- Cuenta de AWS con permisos adecuados
- Dispositivos IoT meteorológicos configurados
- Conocimientos básicos de servicios AWS

## Distribución de Costos Mensuales AWS

| Servicio AWS | Porcentaje | Costo Mensual (USD) |
|--------------|------------|---------------------|
| Kinesis | 31.6% | $11.00 |
| QuickSight | 25.9% | $9.00 |
| Athena | 14.4% | $5.00 |
| Glue | 8.6% | $3.00 |
| S3 | 6.6% | $2.30 |
| Lambda | 5.7% | $2.00 |
| CloudWatch | 5.7% | $2.00 |
| Otros | 1.4% | $0.50 |
| **Total** | **100%** | **$34.80** |

## 📊 Arquitectura del Sistema

```mermaid
flowchart TD
    A[📁 Archivo CSV IoT<br/>iot_telemetry_data.csv] --> B[📤 Script Python<br/>envía datos]
    B --> C[⚡ Kinesis Data Stream<br/>meteo-data-stream]
    C --> D[λ Lambda Function<br/>procesador-datos-meteo]
    D --> E{📂 Amazon S3<br/>Data Lake 3 Capas}
    
    E --> F[🟡 Capa RAW<br/>JSON formato original<br/>s3://.../raw/]
    E --> G[🟢 Capa PROCESSED<br/>Parquet transformado<br/>s3://.../processed/]
    E --> H[🔵 Capa CURATED<br/>Parquet agregado<br/>s3://.../curated/]
    
    F --> I[🔍 AWS Glue Crawler<br/>meteorological_db]
    G --> I
    H --> I
    
    I --> J[🗃️ Glue Data Catalog<br/>Tablas: raw_raw, processed_meteo,<br/>curated_analisis_limpio]
    
    J --> K[📊 Amazon Athena<br/>Consultas SQL]
    J --> L[📈 Amazon QuickSight<br/>Dashboards]
    
    K --> M[🔍 Análisis con SQL<br/>Promedios, agrupaciones,<br/>detección de anomalías]
    L --> N[📱 Visualizaciones<br/>Gráficos, KPIs, tablas<br/>interactivas]

