package breakout;
import java.io.IOException;

public class BreakOut {

    public static void main(String[] args) throws IOException {
        //game elements
        Settings settings = new Settings();
        Bar bar = new Bar(settings);
        Status status = new Status();
        Ball ball = new Ball(settings, bar, status);
        KeyEvents keyEvent = new KeyEvents(settings, bar, ball, status);
        Screen screen = new Screen(settings, keyEvent);
        Button button = new Button(settings);
        RunGame breakOut = new RunGame(bar, settings, screen, ball, status, button);
        
        //running...
        while(true){
            breakOut.render();
            settings.clock(100);
        }
    }
    
}
