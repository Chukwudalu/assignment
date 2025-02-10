
from mainmenu import MainMenu
from helpers import initial_options



def main():
    main_menu = MainMenu()
    menu_on = True
    
    while menu_on:
        try:
            main_menu_selection = initial_options().lower()
            main_menu.handle_incorrect_selection(main_menu_selection)
            main_menu.handle_menu_selection()

            if main_menu.return_to_main_menu:
                continue

            
        except ValueError as e:
            print(e)
        
        except KeyboardInterrupt:
            print('\nProgram Exited')
            menu_on = False

main()