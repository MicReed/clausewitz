from typing import Optional

def greet(name: Optional[str] = None) -> None:
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello, world!")