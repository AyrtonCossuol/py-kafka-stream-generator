from src.utils.generate_data_fake import GenerateDatafake

class StartFlowGenerator:
    def __init__(self) -> None:
        self.data = GenerateDatafake
        self.process()

    def process(self):
        print(self.data.generate_json_fake())
