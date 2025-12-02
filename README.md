# 🌤️ AWS Data Lake: Procesamiento de datos IoT meteorológicos en tiempo real

## 🎯 Descripción del Proyecto
Sistema de Data Lake completamente serverless en AWS para ingerir, procesar, transformar (ETL) y analizar datos meteorológicos IoT en tiempo real. Implementa arquitectura de 3 capas (Raw/Processed/Curated).

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
    
    M --> O[📊 Resultados de Análisis]
    N --> O
    
    O --> P[📄 Documentación Técnica<br/>10-15 páginas]
    O --> Q[🎥 Demostración Final<br/>Video 10-15 min]
    O --> R[🗣️ Presentación<br/>15 min + Q&A]

    style A fill:#e1f5fe
    style B fill:#bbdefb
    style C fill:#90caf9
    style D fill:#64b5f6
    style E fill:#fff3e0
    style F fill:#ffecb3
    style G fill:#ffe082
    style H fill:#ffd54f
    style I fill:#f3e5f5
    style J fill:#e1bee7
    style K fill:#c8e6c9
    style L fill:#fff8e1
    style M fill:#b3e5fc
    style N fill:#ffecb3
    style O fill:#ffebee
    style P fill:#fce4ec
    style Q fill:#e8eaf6
    style R fill:#e3f2fd
