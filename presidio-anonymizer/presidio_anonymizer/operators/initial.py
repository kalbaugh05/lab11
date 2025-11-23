import re
from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.entities import OperatorConfig

class Initial(Operator):
    def __init__(self):
        super().__init__()

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        # Must return the OperatorType enum
        return OperatorType.Anonymize

    def validate(self, operator_config: OperatorConfig) -> None:
        # No special validation needed
        pass

    def operate(self, text: str) -> str:
        parts = text.split()
        initials_list = []

        for part in parts:
            # Find the first alphanumeric character
            match = re.search(r'\w', part)
            if match:
                idx = match.start()
                # Preserve leading symbols, capitalize the first alnum, add dot
                initials_list.append(part[:idx] + part[idx].upper() + ".")
            else:
                # If no alphanumeric character, keep part as-is
                initials_list.append(part)

        return " ".join(initials_list)
