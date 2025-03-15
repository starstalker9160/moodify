class InitializationErr(Exception):
    """Go ahead, take a wild guess on when this error is raised..."""

    def __init__(self, message="App unable to initialize", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message