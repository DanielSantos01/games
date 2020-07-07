package breakout;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;


public class RunGame {
    Bar bar;
    Settings settings;
    Graphics2D g;
    Screen screen;
    Ball ball;
    public RunGame(Bar ba, Settings set, Screen scr, Ball bal){
        bar = ba;
        settings = set;
        screen = scr;
        ball = bal;
    }
    
    public void render(){
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        g = (Graphics2D) bs.getDrawGraphics();
        
        screen.fillBackground(g);
        
        bar.draw(g);
        
        ball.checkEdges();
        ball.draw(g);
        ball.checkMove();
        
        g.dispose();
        bs.show();
    }
}
