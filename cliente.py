import socket 
ip = input('digite o ip de conexao: ') 
port = 7000 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
print("digite uma mensagem para enviar ao servidor\n")
mensagem = input("-> ")
##msg = byte(mensagem)
msg = bytes(mensagem, 'utf-8')
client_socket.send(msg) 
print ("mensagem enviada") 
client_socket.close()