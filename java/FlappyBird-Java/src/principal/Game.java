package principal;  

import java.io.IOException;

public class Game {
    
    public static void main(String[] args) throws IOException{
        
        Settings settings = new Settings();
        Stats stats = new Stats(settings);
        Background backGround = new Background(settings);
        Ground ground = new Ground(settings);
        Bird bird = new Bird(settings, ground, stats);
        KeyEvents key = new KeyEvents(settings,bird);
        Screen screen = new Screen(settings, key);
        WaitScreen waitScreen = new WaitScreen(settings);
        Pipe pipe = new Pipe(settings, bird, stats);
       
        RunGame flappyBird = new RunGame(settings, backGround, ground, screen, waitScreen, bird, pipe, stats);
        flappyBird.start();
        
    }
}
