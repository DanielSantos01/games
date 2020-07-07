package breakout;
import java.awt.Graphics2D;
import java.io.IOException;

public class BreakOut {

    public static void main(String[] args) throws IOException {
        //game elements
        Settings settings = new Settings();
        Bar bar = new Bar(settings);
        Ball ball = new Ball(settings);
        KeyEvents keyEvent = new KeyEvents(settings, bar, ball);
        Screen screen = new Screen(settings, keyEvent);
        Graphics2D g = (Graphics2D) settings.canvas.getGraphics();
        RunGame run = new RunGame(bar, settings, screen, ball);
        
        //running...
        while(true){
            run.render();
            settings.clock(30);
        }
    }
    
}
