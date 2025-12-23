class Player:
    def __init__(self, name: str, num: int):
        self._name = name
        self._num = num
        
    def __str__(self):
        return f"{self._name} is player {self._num}"
    
    @property
    def name(self):
        return self._name
    
    @property
    def number(self):
        return self._num
    