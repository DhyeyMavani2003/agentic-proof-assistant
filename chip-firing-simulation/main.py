from dollar_game import DollarGame

def main():
    # Define the graph and divisor
    graph = {
        'A': {'B': 1, 'C': 1, 'E': 2},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1, 'E': 1},
        'E': {'A': 2, 'C': 1}
    }
    divisor = {'A': 2, 'B': -3, 'C': 4, 'E': -1}

    # Create a DollarGame instance
    game = DollarGame(graph, divisor)

    # Play the game
    winnable, firing_script = game.play_game()

    # Output results
    if winnable:
        print("The game is winnable.")
        print("Firing Script:", dict(firing_script))

        # Apply the Laplacian matrix to verify the result
        resulting_divisor = game.apply_laplacian(firing_script)
        print("Resulting Divisor:", dict(resulting_divisor))
    else:
        print("The game is not winnable.")

if __name__ == "__main__":
    main()