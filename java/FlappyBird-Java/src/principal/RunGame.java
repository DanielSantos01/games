package principal;

import java.awt.Graphics;
import java.awt.image.BufferStrategy;

public class RunGame extends Thread{
    private final Settings settings;
    private final Background background;
    private final Ground ground;
    private final Screen screen;
    private final WaitScreen waitScreen;
    private final Bird bird;
    private Graphics g;
    private final Pipe pipe;
    private final int fps;
    
    public RunGame(Settings set, Background bg, Ground gnd, Screen scr, WaitScreen ws, Bird brd, Pipe pp){
        settings = set;
        background = bg;
        ground = gnd;
        screen = scr;
        waitScreen = ws;
        bird = brd;
        pipe = pp;
        fps = 30;
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    @Override
    public void run(){
        
        while(true) render();
        
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void render(){
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        g = bs.getDrawGraphics();
        updateScreen();
        g.dispose();
        bs.show();
    }
    
    private void updateScreen(){
        settings.clock(fps);
        background.drawBackground(g);
        pipe.draw(g);
        if(settings.preStart || settings.gameOver) pauseScreen();
        bird.run(g);
        ground.display(g);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void pauseScreen(){
        waitScreen.draw(g);
    }
}
