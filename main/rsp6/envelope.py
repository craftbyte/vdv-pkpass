import dataclasses
import base26
from . import util, pki


@dataclasses.dataclass
class Envelope:
    issuer_id: str
    ticket_ref: str
    payload: bytes

    @classmethod
    def parse(cls, data: bytes) -> "Envelope":
        if len(data) < 16:
            raise util.RSP6Exception("Envelope is too short")

        if data[0:2] != b"06":
            raise util.RSP6Exception("Envelope isn't an RSP6 ticket")

        try:
            ticket_ref = data[2:11].decode()
            issuer_id = data[13:15].decode()
        except UnicodeDecodeError as e:
            raise util.RSP6Exception("Invalid ticket reference encoding") from e

        try:
            payload = base26.decode(data[15:].decode())
        except UnicodeDecodeError as e:
            raise util.RSP6Exception("Invalid payload encoding") from e

        return cls(
            issuer_id=issuer_id,
            ticket_ref=ticket_ref,
            payload=payload,
        )

    def decrypt_with_cert(self, cert: pki.Certificate) -> bytes:
        h = int.from_bytes(self.payload, 'big')
        m = pow(h, cert.exponent, cert.modulus)
        data = m.to_bytes(cert.modulus_len, 'big')

        if data[0] == 0 and data[1] == 1:
            offset = 2
            while data[offset] == 0xFF:
                offset += 1
            if data[offset] == 0:
                return data[offset+1:]
