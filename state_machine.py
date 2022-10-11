from itertools import cycle
from typing import Iterable, Optional


class StateMachine:
    def __init__(self, states: Iterable):
        self.__states_cycle = cycle(states)
        self.__current_machine_state: Optional[str] = None

    def set_next_state(self):
        self.__current_machine_state = str(next(self.__states_cycle))

    @property
    def current_state(self) -> str:
        if not self.__current_machine_state:
            self.set_next_state()

        return self.__current_machine_state
