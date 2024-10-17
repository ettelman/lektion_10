# import zipfile

## Skapa en zipfil
# def create_zip(zip_filename, files_to_zip):
#     with zipfile.ZipFile(zip_filename, "w") as zipf:
#         for file in files_to_zip:
#             zipf.write(file, arcname=file.split('/')[-1])
#     print(f"Skapade en zipfil: {zip_filename}")

# files = ["test1.txt", "test2.txt"]
# create_zip('test.zip', files)

## Extrahera zipfil
# def extract_zip(zip_filename, extract_to):
#     with zipfile.ZipFile(zip_filename, 'r') as zipf:
#         zipf.extractall(extract_to)
#     print(f"Extraherade alla filer till {extract_to}")

# extract_zip('test.zip', 'socket')

# def read_zip(zip_filename):
#     with zipfile.ZipFile(zip_filename, 'r') as zipf:
#         file_list = zipf.namelist()
#     print(file_list)

# read_zip('test.zip')

# import shutil

# shutil.make_archive(zip_filename, 'zip', 'socket')
# shutil.unpack_archive(zip_file, extra_to)

## Zipfil med lösenord
# def create_zip(zip_filename, files_to_zip, password):
#     with zipfile.ZipFile(zip_filename, 'w') as zipf:
#         for file in files_to_zip:
#             zipf.write(file, arcname=file.split('/')[-1])
#         for file in zipf.namelist():
#             zipf.setpassword(password.encode())
#     print(f"Skapade en zipfil: {zip_filename}")

# files = ["test1.txt", "test2.txt"]
# create_zip("test.zip", files, "password123")

## Threads ##

# import threading
# import time

# def count_numbers():
#     for i in range(1,6):
#         print(i)
#         time.sleep(1)

# def write_message():
#     for i in range(1,6):
#         print("Hej")
#         time.sleep(1.2)

# thread1 = threading.Thread(target=count_numbers)
# thread2 = threading.Thread(target=write_message)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Klara!")

# counter = 0
# counter_lock = threading.Lock()

# def counter_fun():
#     global counter
#     for i in range(10000):
#         with counter_lock:
#             counter += 1

# threads = []
# for i in range(5):
#     thread = threading.Thread(target=counter_fun)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print(counter)

## Zip med lösenord

# import pyminizip

# def create_zip(zip_filename, files_to_zip, password):
#     for file in files_to_zip:
#         pyminizip.compress(file, None, zip_filename, password, 5)
#     print(f"Skapat zip: {zip_filename}")

# files = ["test1.txt", "test2.txt"]
# password = "password123"
# create_zip('test.zip', files, password)

# sniffed_packets = sniff(count=20)
# sniffed_packets.summary()

# packet = IP(dst='8.8.8.8')/TCP(dport=80)
# packet.show()

from scapy.all import *

domain = "www.example.com"

dns_request = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain))

response = sr1(dns_request, timeout=2)

if response.haslayer(DNS):
    for i in range(response[DNS].ancount):
        answer = response[DNS].an[i]
        print(answer.rdata)
else:
    print(f"Fick inget svar för {domain}")