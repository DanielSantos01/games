package principal;

import java.awt.Canvas;

public class Settings {
    //constantes
    protected final int screenWidth;
    protected final int screenHeight;
    protected final int birdUpValue;
    protected final int gravity;
    protected final int frames;
    //variável
    protected int fall;
    //flags
    protected boolean preStart;
    protected boolean start;
    protected boolean gameOver;
    protected final int pipeUpHeight[] = {100, 50, 30, 150, 300, 70, 180, 200, 120, 60};
    protected volatile boolean drawBackground;
    protected volatile boolean drawGame;
    protected volatile boolean drawBird;
    protected volatile boolean drawGround;
    protected volatile boolean configurePipes;
    protected Canvas canvas;
    
    public Settings(){
        //screen
        screenWidth = 400;
        screenHeight = 680;
        frames = 30;
        
        //bird settings
        birdUpValue = -8;
        fall = 10;
        gravity = 1;
        
        //set flags
        preStart = true;
        configurePipes = true;
        start = false;
        gameOver = false;
        drawBackground = true;
        drawGame = false;
        
        //canvas
        canvas = new Canvas();
        canvas.setSize(400, 680);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void clock(int frames){
        long agora = System.currentTimeMillis();
        while ((System.currentTimeMillis() - agora) <= (1000/frames)){}
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void wait(float time){
        long agora = System.currentTimeMillis();
        while ((System.currentTimeMillis() - agora) < time){}
    }
    
}
