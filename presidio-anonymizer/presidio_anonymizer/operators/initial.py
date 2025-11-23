from presidio_anonymizer.operators import Operator

class Initial(Operator):
    def __init__(self):
        super().__init__()

    def operate(self, text: str) -> str:
        # Minimal implementation for now, just return text
        return text

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> str:
        # This tells the engine it’s an anonymizer
        return "anonymize"

    def validate(self, params: dict) -> None:
        # Minimal: accept any params
        pass
