"""
ESCAPE THE LIBRARY
Mini text adventure game written in Python.

The player explores a mysterious library, finds clues and objects,
then tries to escape through a hidden passage.
"""

# =========================
# GAME INTRODUCTION
# =========================

print("=== ESCAPE THE LIBRARY ===")
print("You wake up in a mysterious library.")
print("A voice whispers: 'Find the hidden exit...'")

# Global inventory used by all rooms
inventory = []


# =========================
# MAIN HUB
# =========================

def library():
    """
    Central room of the game.
    The player chooses which area to explore.
    """

    print("\nYou are in the central library.")
    print("1 - Archives")
    print("2 - Botanical Garden")
    print("3 - Secret Laboratory")

    choice = input("Choose a door: ")

    if choice == "1":
        archives()
    elif choice == "2":
        garden()
    elif choice == "3":
        laboratory()
    else:
        print("Invalid choice.")
        library()


# =========================
# ARCHIVES
# =========================

def archives():
    """
    The player can discover the hidden stone door.
    A silver key is required to open it.
    """

    print("\nDusty books surround you.")
    print("1 - Return to library")
    print("2 - Search deeper")

    choice = input("Choose: ")

    if choice == "1":
        library()

    elif choice == "2":
        print("\nYou discover a strange stone door.")
        print("A moon-shaped lock is carved into the door.")

        # Check if the player owns the key
        if "silver key" in inventory:
            print("\nThe silver key fits perfectly into the lock.")
            print("The heavy stone door slowly opens...")
            print("You discovered a hidden passage!")

            choice = input("Enter? (yes/no): ")

            if choice == "yes":
                hidden_passage(1)

            elif choice == "no":
                print("The walls are closing on you!")
                game_over()

            else:
                print("Invalid answer.")
                archives()

        else:
            print("You need a silver key to unlock it.")

            choice = input("Explore the other doors? (yes/no): ")

            if choice == "yes":
                library()

            elif choice == "no":
                game_over()

            else:
                print("Invalid answer.")
                archives()

    else:
        print("Invalid choice.")
        archives()


# =========================
# BOTANICAL GARDEN
# =========================

def garden():
    """
    The player can find the silver key in the greenhouse.
    Choosing the wrong side results in death.
    """

    print("\nA warm golden light fills the botanical garden.")
    print("An old greenhouse and a fountain catch your attention.")

    print("\n1 - Explore the greenhouse")
    print("2 - Examine the fountain")

    choice = input("Choose: ")

    # -------- Greenhouse --------
    if choice == "1":
        print("\nLeft - Strange flowers grow in the dark.")
        print("Right - Beautiful flower pots are displayed near the window.")

        direction = input("Where do you want to go? (left/right): ")

        if direction == "left":
            print("\nThe flowers release toxic spores...")
            game_over()

        elif direction == "right":

            # Prevents adding the key multiple times
            if "silver key" not in inventory:
                print("\nYou discover a dusty silver key hidden beneath a flower pot.")
                print("\033[1mSilver Key added to your inventory.\033[0m")
                inventory.append("silver key")
            else:
                print("\nYou already took the silver key.")

            input("\nPress Enter to return to the library...")
            library()

        else:
            print("\nInvalid answer.")
            garden()

    # -------- Fountain --------
    elif choice == "2":
        print("\nThe fountain is dry. Nothing seems unusual.")

        back = input("Go back? (yes/no): ")

        if back == "yes":
            garden()
        elif back == "no":
            library()
        else:
            print("Invalid answer.")
            garden()

    else:
        print("Invalid choice.")
        garden()


# =========================
# LABORATORY
# =========================

def laboratory():
    """
    The laboratory contains the journal and the oil lamp,
    both necessary to understand the hidden passage.
    """

    while True:
        print("\nYou enter an abandoned laboratory.")

        print("\nWhat would you like to do?")
        print("1 - Search the shelves")
        print("2 - Examine the desk")
        print("3 - Return to the library")

        choice = input("Choose: ")

        if choice == "1":
            print("\nMost of the books have crumbled away, but one page catches your eye:")
            print("\033[1m'The hidden passage has remained in darkness for centuries.'\033[0m")

        elif choice == "2":
            desk()

        elif choice == "3":
            library()

        else:
            print("Invalid choice.")


# =========================
# DESK
# =========================

def desk():
    """
    The player can read the journal or take the oil lamp.
    """

    print("\nThe desk is covered in dust.")
    print("An old journal lies open beside an unlit oil lamp.")

    print("\nWhat would you like to do?")
    print("1 - Read the journal")
    print("2 - Take the oil lamp")
    print("3 - Return")

    choice = input("Choose: ")

    if choice == "1":
        print("\n\033[1;4mThe Aurelian Journal\033[0m")
        print("\033[3mOctober 17, 1894\033[0m")
        print(
            "\033[1mThe secret passage may only be crossed with light. "
            "Never turn around once you enter, or the corridor will claim you.\033[0m"
        )

    elif choice == "2":

        if "oil lamp" not in inventory:
            print("\033[1m'Oil lamp' has been added to your inventory.\033[0m")
            inventory.append("oil lamp")
        else:
            print("You already took the oil lamp.")

    elif choice == "3":
        return

    else:
        print("Invalid answer.")


# =========================
# HIDDEN PASSAGE
# =========================

def hidden_passage(level=1):
    """
    Recursive function representing the descent into the hidden tunnel.

    level = current depth of the passage.
    The player wins at depth 3.
    """

    print("\nThe passage is completely dark.")

    # The lamp is mandatory
    if "oil lamp" not in inventory:
        print("\nWithout a source of light, it is too dangerous to continue.")

        choice = input("Continue anyway? (yes/no): ")

        if choice == "yes":
            print("\nYou have been swallowed by the darkness.")
            game_over()

        elif choice == "no":
            print("\033[1mYou should search the other rooms for clues.\033[0m")
            library()

        else:
            print("Invalid answer.")
            hidden_passage(level)

        return

    # If the player has the lamp
    print("\nYou light the oil lamp.")
    print("The hidden passage stretches deep beneath the library...")
    print(f"\nPassage depth: {level}")

    # Different descriptions depending on depth
    if level == 1:
        print("\nThe air is cold and damp.")

    elif level == 2:
        print("\nThe tunnel narrows around you.")
        print("A whisper seems to call your name.")

    elif level == 3:
        print("\nA warm breeze reaches your face.")
        print("A beam of sunlight appears ahead.")
        print("You found the hidden exit!")
        victory()
        return

    print("\n1 - Go deeper")
    print("2 - Turn around")

    choice = input("Choose: ")

    if choice == "1":

        # Recursive call: go one level deeper
        hidden_passage(level + 1)

    elif choice == "2":
        print("\nYOU MUST NEVER TURN AROUND!")
        game_over()

    else:
        print("Invalid choice.")
        hidden_passage(level)


# =========================
# ENDINGS
# =========================

def victory():
    """Victory screen."""

    print("\n========================================")
    print("\033[1mYOU ESCAPED THE LIBRARY! CONGRATULATIONS!\033[0m")
    print("========================================")


def game_over():
    """
    Defeat screen and replay management.
    The inventory is reset when a new game starts.
    """

    global inventory

    print("\n_________")
    print("\033[1mGAME OVER\033[0m")
    print("_________")

    print("\nYou failed to escape...")

    replay = input(
        "\033[1mPlay again?\033[0m (yes/no): "
    )

    if replay == "yes":

        # Reset inventory for a fresh game
        inventory = []
        library()

    else:
        print("\033[1mGoodbye!\033[0m")


# =========================
# GAME START
# =========================

library()