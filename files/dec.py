import base64
import Crypto

#rom Crypto.Cipher import AES
encoded = "ksP5VVZiCnGwKKmb/hasBE0hwd8kLILZTQV4Jz544TUjqGv1x0MccWrrWmptFhzJNzcoUR/dvCLwlEri30dsKqJ+jlxeRQ2vFBcVqACwJiYDDaPumurScCNsTxmSPeckzqyivNB3RVJJV1FOWEx1yy7vjpGUN4x8kG44Q7oXJtP35QwzMPV79XEJsXDMS0wTacGm4dRFDmxeggK1i0Dxwg=="

#decoded = base64.b64decode(encoded)
decoded = cipher.decrypt(base64.b64decode(encoded))
print(decoded)
