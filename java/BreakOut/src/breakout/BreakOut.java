package breakout;
import java.awt.Graphics2D;
import java.io.IOException;

public class BreakOut {

    public static void main(String[] args) throws IOException {
        Settings settings = new Settings();
        Bar bar = new Bar(settings);
        KeyEvents keyEvent = new KeyEvents(settings, bar);
        Screen screen = new Screen(settings, keyEvent);
        Graphics2D g = (Graphics2D) settings.canvas.getGraphics();
        RunGame run = new RunGame(bar, settings);
        
        while(true){
            run.render();
        }
    }
    
}
