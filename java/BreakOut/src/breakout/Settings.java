package breakout;
import java.awt.Canvas;

public class Settings {
    protected final int screenWidth;
    protected final int screenHeight;
    protected Canvas canvas;
    protected boolean preStart;
    protected boolean start;
    protected boolean buildWall;
    protected boolean remove;
    protected boolean gameOver;
    
    public Settings(){
        screenWidth = 1000;
        screenHeight = 600;
        canvas = new Canvas();
        preStart = true;
        start = false;
        buildWall = true;
        remove = false;
        gameOver = false;
    }
    
    public void clock(int frames){
        long agora = System.currentTimeMillis();
        while ((System.currentTimeMillis() - agora) <= (1000/frames)){}
    }
}
