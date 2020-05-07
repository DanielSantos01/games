package principal;  
import java.io.IOException;

public class Game {
    
    public static void main(String[] args) throws IOException{
        
        //--------------------------------------------------------------------------------------------------------------------
        Settings settings = new Settings();
        Background back = new Background(settings);
        Ground ground = new Ground(back, settings);
        Bird bird = new Bird(settings, ground);
        KeyEvents key = new KeyEvents(settings,bird);
        Screen screen = new Screen(settings, key);
        WaitScreen waitScreen = new WaitScreen(settings);
        UpdateScreen updateScreen = new UpdateScreen();
        
        //--------------------------------------------------------------------------------------------------------------------
        RunGame runGame = new RunGame(settings, back, ground, screen, updateScreen, waitScreen, bird);
        runGame.start();
        
    }
}
