# Docker ile Cassandra Python Entegrasyonu

Bu proje, Docker ortamında çalışan bir **Cassandra veritabanından** verilerin nasıl okunacağını gösteren basit ama işlevsel bir örnektir.

## Özellikler

- Cassandra veritabanı Docker konteynerinde çalışır.
- Python (3.9) başka bir konteynerde Cassandra'ya bağlanır.
- `cassandra-driver` paketi ile veri okuma gerçekleştirilir.
- Veriler terminalde yazdırılır.

## Kullanım

1. Cassandra konteyneri çalıştırılır ve `deneme` adında bir keyspace ile `ogrenciler` tablosu oluşturulur.
2. Python konteyneri çalıştırılarak veriler okunur.

## Dosyalar

- `cassandra_read.py`: Cassandra'dan veri okuyan Python dosyası.
- `Dockerfile`: Python konteyneri için yapılandırma.
