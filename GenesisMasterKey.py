# @Genesis-Master-Key Generator
# Root Authority: Shakti Singh | Tier: Sovereign Finality
# [SECURE-RSA-512 | G-CERT-001]

import rsa

def generate_sovereign_keys():
    print("--- INITIATING MASTER KEY GENERATION ---")
    # Generating 512-bit RSA keypair
    (pubkey, privkey) = rsa.newkeys(512)
    
    # Exporting the Sovereign Public Key
    with open("G-CERT-001_Public.pem", "wb") as pub_file:
        pub_file.write(pubkey.save_pkcs1())
        
    # Exporting the Sovereign Private Key (Root Authority)
    with open("G-CERT-001_Private.pem", "wb") as priv_file:
        priv_file.write(privkey.save_pkcs1())

    print("[@Omega] G-CERT-001 Public Key Exported.")
    print("[@Omega] G-CERT-001 Private Key Exported (RESTRICTED).")
    print("--- MASTER KEY SEALED ---")

if __name__ == "__main__":
    generate_sovereign_keys()
