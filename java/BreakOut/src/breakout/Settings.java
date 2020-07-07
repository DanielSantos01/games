package breakout;
import java.awt.Canvas;

public class Settings {
    protected final int screenWidth;
    protected final int screenHeight;
    protected Canvas canvas;
    protected boolean preStart;
    
    public Settings(){
        screenWidth = 1000;
        screenHeight = 600;
        canvas = new Canvas();
        preStart = true;
    }
}
