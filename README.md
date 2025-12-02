# 🌤️ AWS Data Lake: Procesamiento de Datos IoT Meteorológicos en Tiempo Real

## 🎯 Descripción del Proyecto
Sistema de Data Lake completamente serverless en AWS para ingerir, procesar, transformar y analizar datos meteorológicos IoT en tiempo real. Implementa arquitectura de 3 capas (Raw/Processed/Curated) siguiendo las mejores prácticas del Well-Architected Framework.

## 📊 Arquitectura del Sistema

```mermaid
graph TD
    A[📁 CSV IoT] --> B[📤 Python Script]
    B --> C[⚡ Kinesis Data Stream]
    C --> D[λ Lambda Function]
    D --> E{📂 S3 Data Lake}
    
    E --> F[🟡 Capa RAW - JSON]
    E --> G[🟢 Capa PROCESSED - Parquet]
    E --> H[🔵 Capa CURATED - Agregados]
    
    F --> I[🔍 Glue Crawler]
    I --> J[🗃️ Glue Data Catalog]
    
    J --> K[📊 Athena - SQL Analytics]
    J --> L[📈 QuickSight - Dashboards]
