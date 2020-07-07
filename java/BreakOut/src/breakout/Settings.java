package breakout;
import java.awt.Canvas;

public class Settings {
    protected final int screenWidth;
    protected final int screenHeight;
    protected Canvas canvas;
    protected boolean preStart;
    protected boolean start;
    
    public Settings(){
        screenWidth = 1000;
        screenHeight = 600;
        canvas = new Canvas();
        preStart = true;
        start = false;
    }
    
    public void clock(int frames){
        long agora = System.currentTimeMillis();
        while ((System.currentTimeMillis() - agora) <= (1000/frames)){}
    }
}
