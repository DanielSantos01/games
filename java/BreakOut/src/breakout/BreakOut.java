package breakout;
import java.io.IOException;

public class BreakOut {

    public static void main(String[] args) throws IOException {
        //game elements
        Settings settings = new Settings();
        Bar bar = new Bar(settings);
        Score score = new Score();
        Ball ball = new Ball(settings, bar, score);
        KeyEvents keyEvent = new KeyEvents(settings, bar, ball, score);
        Screen screen = new Screen(settings, keyEvent);
        Button btn = new Button(settings);
        RunGame breakOut = new RunGame(bar, settings, screen, ball, score, btn);
        
        //running...
        while(true){
            breakOut.render();
            settings.clock(100);
        }
    }
    
}
