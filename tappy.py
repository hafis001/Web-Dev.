class ButtonGame:
    def __init__(self):
        self.points = 0
        self.level = 1

    def click_button(self):
        self.points += 1
        print("Point added! Current points:", self.points)
        if self.points >= self.level * 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        print("Congratulations! You reached level", self.level)

def main():
    game = ButtonGame()
    while True:
        print("Press 'c' to click the button or 'q' to quit.")
        choice = input().lower()
        if choice == 'c':
            game.click_button()
        elif choice == 'q':
            print("Game over. Final points:", game.points)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
