# My Art Gallery Collection Manager (ACP starter, DSCM2L4). Python 3 standard library only.
# Run it as art_gallery_manager.py (or in one Colab cell): type a menu number and press Enter.
# It runs now (choose 4 to quit). Do TODO 1 to TODO 4 in order. (given) lines are done for you.


class ArtGallery:
    def __init__(self, gallery_name, city):
        # TODO 1: store gallery_name and city on self, start self.artworks as a
        #   new empty list, then print "<gallery_name> in <city> is open."
        #   Check: "Little Brushes Gallery in Portland is open."
        self.gallery_name, self.city = "Untitled", "?"  # (given) placeholder: replace this line
        self.artworks = ["(no artworks: write TODO 1)"]  # (given) placeholder: replace this line

    def add_artwork(self, title):
        # TODO 2: reject an empty title with "Title cannot be empty."; otherwise
        #   append it and print "'<title>' added."
        #   Check: "'Sunflowers by Maria' added."
        print("add_artwork is not written yet")  # (given) placeholder: replace this line

    def remove_artwork(self, title):
        # TODO 3: remove the title only if it is in the list and print
        #   "'<title>' removed."; otherwise print "'<title>' is not in the gallery."
        #   Check: removing a missing title prints the message, no crash.
        print("remove_artwork is not written yet")  # (given) placeholder: replace this line

    def show(self):                                            # (given) A
        print(f"{self.gallery_name}, artworks: {len(self.artworks)}", self.artworks)

    # TODO 4: add __del__ that prints "Closing <gallery_name>. Goodbye!"
    #   Check: choosing 4 prints the closing line.


gallery = ArtGallery("Little Brushes Gallery", "Portland")        # (given) B
while True:                                                    # (given) C: menu
    choice = input("\n1. Add  2. Remove  3. Show  4. Close\nChoice: ").strip()
    if choice == "1":
        gallery.add_artwork(input("Title: ").strip())
    elif choice == "2":
        gallery.remove_artwork(input("Title to remove: ").strip())
    elif choice == "3":
        gallery.show()
    elif choice == "4":
        del gallery
        break
    else:
        print("Please type 1, 2, 3 or 4.")
