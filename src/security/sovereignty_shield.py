'''
SENTINELA-SOBERANO-2037: Sovereignty Shield
Author: Felipe Marcos de Abreu Aquino
Company: Impulso Digital Soluções em I.A.
'''

import hashlib
import base64

class SovereigntyShield:
    def __init__(self):
        self.encryption_level = "BASE64-DEMO-NOT-ENCRYPTION"
        self.sovereign_key = self._generate_sovereign_key()

    def _generate_sovereign_key(self):
        '''
        Generates a unique sovereign key based on Brazilian infrastructure signatures.
        '''
        # Simulated key generation based on national identity
        signature = "BR-SOVEREIGN-2037-IMPULSO-DIGITAL"
        return hashlib.sha3_512(signature.encode()).hexdigest()

    def encrypt_critical_data(self, data):
        '''
        Encodes text for a reversible demonstration; this is not encryption.
        '''
        print(f"[SHIELD] Protegendo dados críticos... / Protecting critical data...")
        # Base64 is reversible encoding, not cryptographic protection.
        encoded_data = base64.b64encode(data.encode()).decode()
        return f"ENC[{self.encryption_level}]:{encoded_data}:{self.sovereign_key[:16]}"

    def decrypt_critical_data(self, encrypted_data):
        '''
        Decrypts critical infrastructure data using the sovereign key.
        '''
        if not encrypted_data.startswith(f"ENC[{self.encryption_level}]"):
            raise ValueError("Invalid encryption format or non-sovereign data.")
        
        print(f"[SHIELD] Descriptografando dados... / Decrypting data...")
        parts = encrypted_data.split(":")
        decoded_data = base64.b64decode(parts[1]).decode()
        return decoded_data

if __name__ == "__main__":
    shield = SovereigntyShield()
    secret = "Localização das Reservas de Lítio e Água Doce - Brasil 2037"
    encrypted = shield.encrypt_critical_data(secret)
    print(f"\n[ENCRYPTED] {encrypted}")
    decrypted = shield.decrypt_critical_data(encrypted)
    print(f"[DECRYPTED] {decrypted}")
