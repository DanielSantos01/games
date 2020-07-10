package principal;

import java.awt.Graphics;
import java.awt.image.BufferStrategy;

public class RunGame extends Thread{
    private Graphics g;
    private final Settings settings;
    private final Background background;
    private final Ground ground;
    private final Screen screen;
    private final WaitScreen waitScreen;
    private final Bird bird;
    private final Stats stats;
    private final Pipe pipe;
    private final int fps;
    
    public RunGame(Settings set, Background bg, Ground gnd, Screen scr, WaitScreen ws, Bird brd, Pipe pp, Stats stt){
        settings = set;
        background = bg;
        ground = gnd;
        screen = scr;
        waitScreen = ws;
        bird = brd;
        pipe = pp;
        fps = 30;
        stats = stt;
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    @Override
    public void run(){
        while(true) render(); 
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void render(){
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
        if((settings.preStart || settings.gameOver)) waitScreen.draw(g);
        bird.run(g);
        ground.display(g);
        if(settings.start) stats.draw(g);
    }
    
}
