from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

private_key = RSA.import_key(open("private.pem").read())
encode_message = b'vaoBONyT18RLvMFH5PqzXl4Tb7Nl0TSapEuAo82WB9Mw4RkOfJuI3szwK8upVJlq083rADEIEfa7dFmqNrBTOGAX2khvJbrsIFdgeoYsNt9vbRAZrZFRgqfAFj52u0zw/dIX1JzOimlmwY2/xl2gq4yOQfkHyzj0C+qG8opOB81ssbmdGs69++mJ+nBFuDBhyedoeXrUXO30q7PPoX1i3kFlr54LMgwpI9vIDatdB+ggq5lSwFRgaKQhN9AtwB58WUeHN5L2yBlGf7WapqW4Qq4sYQ3nyku7FITN7blrxti1FyYNWLN8ueUSYr3oWcfXiKGnf2LIHaUVy70Yvi8tiw=='
encrypted_message = base64.b64decode(encode_message)
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)
print(decrypted_message.decode())