import sys
from scapy.all import rdpcap
from termcolor import colored

def caesar_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 pcapng_caesar_decrypt.py <pcapng file>")
        sys.exit(1)
        
    pcapng_file = sys.argv[1]

    message = ""
    packets = rdpcap(pcapng_file)
    for packet in packets:
        if packet.haslayer('ICMP'):
            icmp_layer = packet.getlayer('ICMP')
            if icmp_layer.type == 8:  # ICMP request
                first_byte = icmp_layer.load[0]
                message += chr(first_byte)

    highest_score = 0
    most_probable_message = ""
    most_probable_shift = 0

    for shift in range(26):
        decrypted_message = caesar_decrypt(message, shift)
        score = decrypted_message.count(' ') + decrypted_message.count('e') + decrypted_message.count('E')
        
        if score > highest_score:
            highest_score = score
            most_probable_message = decrypted_message
            most_probable_shift = shift

    for shift in range(26):
        decrypted_message = caesar_decrypt(message, shift)
        if shift == most_probable_shift:
            print(colored(f"Shift {shift}: {decrypted_message}", 'green'))
        else:
            print(f"Shift {shift}: {decrypted_message}")


if __name__ == "__main__":
    main()

