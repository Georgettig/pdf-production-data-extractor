import re
from .machine import Machine

class MachineFactory:

    @staticmethod
    def create(filename):

        match = re.search(r"\d+", filename)

        if not match:
            raise ValueError(
                f"Não foi possível identificar o número do arquivo: {filename}"
                )

        num = match.group()

        if len(num) == 8:
            return Machine("MP1")
        
        if len(num) == 9 and num.startswith("2"):
            return Machine("MP2")
        
        raise ValueError(
            f"Máquina não encontrada para o arquivo: {filename}"
        )