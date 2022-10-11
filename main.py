from state_machine import StateMachine

STATES = ("enter_car", "ignite_engine", "accelerate", "drive", "break", "stop engine", "exit_car")


def run():
    st_machine = StateMachine(states=STATES)
    # Current state
    print(st_machine.current_state)
    # One more time - no change
    print(st_machine.current_state)

    # Set new state
    st_machine.set_next_state()
    # Check new state
    print(st_machine.current_state)


if __name__ == "__main__":
    run()
