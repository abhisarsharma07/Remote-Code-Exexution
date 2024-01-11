#IP Address
#protocol TCP/UDP
#socket programming
#number of function
#print(dir(socket))#to see the functions in library
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#s ko use karke socket banana..... #by default it uses TCP protocol #but we have to do through UDP
# ip address , protocol
#finaly s is having capability to create UDP socket
#target system address
target_ip="10.1.0.180"
target_port=9999 #particular name
final_target=(target_ip,target_port) #tuple so that no one can change it
#taking input from user 
msg=input("Please enter your message:")
#since python3 is supporting minimumm encoding method
new_msg=msg.encode('ascii')
#finally lets send data
s.sendto(new_msg,final_target)
print(s.recvfrom(100))