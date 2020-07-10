package alieninvasion;

import java.io.IOException;

public class AlienInvasion {
    
    public static void main(String[] args) throws IOException {
        Settings settings = new Settings();
        Ship ship = new Ship(settings);
        KeyEvents keyEvent = new KeyEvents(ship, settings);
        Screen screen = new Screen(settings, keyEvent);
        RunGame alienInvasion = new RunGame(screen, settings, ship);
        alienInvasion.start();
    }
    
}
