import socket
import csv
import json
results = {}


def is_alive(ip):
    common_ports = [80, 443, 22, 8080] #Check if host is reachable on any of these ports
    for port in common_ports:

        try:
            socket.setdefaulttimeout(1) #Setting a timeout so it doesn't hang forever
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, port)) #Connect to port and ip

            return True  #If reachable on any of the common ports return true
        except:
            continue
    return False

def scan_ports(ip):
    common_ports = [80, 443, 22, 8080] #Define list of ports to test
    open_ports = [] #Create empty list for open ports
    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) #Setting a timeout so it doesn't hang forever
            s.connect((ip,port)) #Connect to port and ip, if no exception raised then port is open
            open_ports.append(port) #Add port to open port list
            s.close() #End connection
        except socket.error:
            print (f'Port {port} is down')
    print(f' Port {open_ports} is open')
    return open_ports #Return open ports list to pass to dictionary

def result_dict(results,status, ip, open_ports): #Print dictionary
    results[ip]= {'status': status,
                  'open_ports': open_ports}
    print (results)
    return results

def export_to_json(results):
    with open('results.json', 'w') as outfile: #Convert results to JSON file

        json.dump(results, outfile, indent=2)

with open ('ips.csv' , 'r' , newline='' ) as file: #Open IP CSV file

    reader = csv.reader(file)
    next (reader) #Skip header row

    for row in reader:
        ip = row[0] #extracts the IP address from the row as a string

        print(f'Checking: {ip}')
        result = is_alive(ip) #Store result - true or false

        if result : #If host alive
            status = "alive"
            open_ports = scan_ports(ip) #check which specific ports are open on the host
            result_dict(results, status, ip, open_ports) #Pass result to dictionary
        else: #If host is dead
            status = "dead"
            result_dict(results,status, ip, []) #Pass empty list to dictionary as there will be no open ports

    export_to_json(results)
