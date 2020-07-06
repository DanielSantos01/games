package breakout;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;


public class RunGame {
    Bar bar;
    Settings settings;
    Graphics2D g;
    public RunGame(Bar ba, Settings set){
        bar = ba;
        settings = set;
    }
    
    public void render(){
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        g = (Graphics2D) bs.getDrawGraphics();
        bar.draw(g);
        g.dispose();
        bs.show();
    }
}
