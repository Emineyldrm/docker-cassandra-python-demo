from cassandra.cluster import Cluster

def main():
    cluster = Cluster(['172.17.0.2'])  # Cassandra IP adresi
    session = cluster.connect('deneme') #kullandığım keyspase
    
    rows = session.execute('SELECT * FROM ogrenciler;')
    for row in rows:
        print(f"id: {row.id}, ad: {row.ad}, soyad: {row.soyad}, yas: {row.yas}")

if __name__ == "__main__":
    main()

