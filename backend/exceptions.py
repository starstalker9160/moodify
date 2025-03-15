class InitializationErr(Exception):
    """Go ahead, take a wild guess on when this error is raised..."""

    def __init__(self, message="App unable to initialize", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message


class InvalidJSONFormat(Exception):
    """Man this one is suuuper obvious... c'mon!"""

    def __init__(self, message="POST request on '/submit' does not have a valid JSON format", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message
