package alieninvasion;

import java.awt.Canvas;

public class Settings {
    protected final int screenWidth;
    protected final int screenHeight;
    protected boolean createFleet;
    protected Canvas canvas;
    
    public Settings(){
        screenWidth = 1000;
        screenHeight = 700;
        canvas = new Canvas();
        canvas.setSize(screenWidth, screenHeight);
        createFleet = true;
    }
    
    
    protected void clock(int frames){
        long agora = System.currentTimeMillis();
        while ((System.currentTimeMillis() - agora) <= (1000/frames)){}
    }
}
