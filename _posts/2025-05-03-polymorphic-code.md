---
title: Polymorphic Code
author: gourabdg47
date: 2025-05-03 00:26:00
categories:
  - Information
  - Code
tags:
  - coding
  - python
render_with_liquid: true
---


#### Sample polymorphic code

###### Explanation:

1. **Polymorphism Technique**: The code uses a unique identifier (hash) combined with random numbers to generate a new signature for each communication.
2. **Variable-Length Encoding (VLE)**: Data is encoded using Base64, but the length of the encoded data changes dynamically based on the unique identifier.
3. **Self-Contained Functionality**: The `polymorphic_encode` function modifies the data by appending or pretending variable-length data, making it difficult to detect a consistent signature.

###### Usage

```python
import random
from base64 import b64encode, b64decode

class PolymorphicMalware:
    def __init__(self):
        self.seed = random.randint(1, 1000)
        self.p_code = "XORshift"
    
    def polymorphic_encode(self, data):
        # Generate a unique identifier for each communication
        unique_id = str(hash(f"{self.seed}{random.randint(1, 10000)}")) + random.choice("0123456789")
        
        # Convert data to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Perform a simple XOR-based encryption using the seed
        encrypted = bytearray()
        for i, byte in enumerate(data):
            key_byte = (self.seed + i) % 256
            encrypted.append(byte ^ key_byte)
        
        # Encode the encrypted data with base64
        encoded_data = b64encode(encrypted)
        
        # Append a unique signature based on the unique_id
        signature = unique_id.encode('utf-8')[:8]  # Use first 8 bytes of unique_id
        
        # Combine the encoded data with the signature
        result = encoded_data + b':' + b64encode(signature)
        
        return result
    
    def polymorphic_decode(self, encoded_data):
        # Split the encoded data and signature
        parts = encoded_data.split(b':')
        if len(parts) != 2:
            raise ValueError("Invalid encoded data format")
        
        # Extract the encoded data without the signature
        data_part = parts[0]
        
        # Decode the base64 data
        encrypted = b64decode(data_part)
        
        # Perform the reverse XOR operation
        decrypted = bytearray()
        for i, byte in enumerate(encrypted):
            key_byte = (self.seed + i) % 256
            decrypted.append(byte ^ key_byte)
        
        return bytes(decrypted)
    
    def send_data(self, destination_ip, data_to_send):
        # Encode the data before sending
        encoded_data = self.polymorphic_encode(data_to_send)
        print(f"Sending polymorphic data to {destination_ip}")
        return encoded_data
    
    def receive_data(self, encoded_data):
        # Decode the received data
        try:
            original_data = self.polymorphic_decode(encoded_data)
            return original_data
        except Exception as e:
            print(f"Error decoding data: {e}")
            return None


# Example usage
if __name__ == "__main__":
    malware = PolymorphicMalware()
    
    # Test with string data
    test_data = "This is sensitive information"
    print(f"Original data: {test_data}")
    
    # Encode and send
    encoded = malware.send_data("192.168.1.100", test_data)
    print(f"Encoded data: {encoded}")
    
    # Receive and decode
    decoded = malware.receive_data(encoded)
    print(f"Decoded data: {decoded.decode('utf-8')}")
    
    # Verify that each encoding is different
    print("\nVerifying polymorphic nature:")
    for _ in range(3):
        encoded = malware.polymorphic_encode(test_data)
        print(f"New encoded form: {encoded}")

```



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }
