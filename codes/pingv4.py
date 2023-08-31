from scapy.all import IP, ICMP, send

def enviar_mensaje_icmp(ip_destino, mensaje):
    relleno = b'\x00\x00\x00\x00\x00\x00\x00'  # Relleno con ceros (8 bytes)
    parte_media = bytes.fromhex("101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637")
    
    for i, caracter in enumerate(mensaje):
        payload_icmp = bytes([ord(caracter)]) + relleno + parte_media
        icmp_packet = IP(dst=ip_destino) / ICMP(type="echo-request", id=1000, seq=i) / payload_icmp
        send(icmp_packet, verbose=False)

mensaje = input("Ingrese el mensaje a enviar: ")
ip_destino = input("Ingrese la dirección IP de destino: ")

enviar_mensaje_icmp(ip_destino, mensaje)
print("Mensajes ICMP enviados.")
